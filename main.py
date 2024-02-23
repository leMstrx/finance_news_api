import requests
import bs4
from stocks_info import stocks_info, stock_symbols
from finbert_utils import estimate_sentiment
import sqlite3
import datetime




def find_related_articles(title, data_p):
    related_stocks = []
    for symbol, names in stock_symbols.items():
        for name in names:
            if name in title or name in data_p:
                related_stocks.append(symbol)
                break  # Stop searching this stock if a match is found
    return related_stocks

def insert_news_update_sentiment(title, url, data_p, sentiment, probability, related_companies, cursor, conn):
    #Check if news already exists 
    cursor.execute("SELECT id FROM news WHERE url = ?", (url,))
    exists = cursor.fetchone()

    if not exists:
        
        #Insert new items
        related_companies_str = ','.join(related_companies)

        cursor.execute('''
        INSERT INTO news(title, url, content, sentiment, probability, related_companies)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, url, data_p, sentiment, probability, related_companies_str))

        #Update daily sentiments
        today = datetime.date.today()
        for company in related_companies:
            cursor.execute('''
            INSERT INTO daily_sentiments(date, stock_symbol, latest_sentiment, latest_probability)
            VALUES (?, ?, ?, ?)
            ON CONFLICT (date, stock_symbol) DO UPDATE SET
                positive_count = CASE WHEN ? = 'positive' THEN positive_count + 1 ELSE positive_count END,
                negative_count = CASE WHEN ? = 'negative' THEN negative_count + 1 ELSE negative_count END,
                neutral_count = CASE WHEN ? = 'neutral' THEN neutral_count + 1 ELSE neutral_count END,
                latest_sentiment = ?,
                latest_probability = ?
            ''', (today, company, sentiment, probability, sentiment, sentiment, sentiment, sentiment, probability))

        conn.commit()

def delete_old_news(cursor, conn):
    #Delete entries older than 2 days
    cursor.execute("DELETE FROM news WHERE timestamp < datetime('now', '-2 days')")
    conn.commit()

def main():
    response = requests.get("https://biztoc.com/")
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    #All SQL Related Settings 
    conn = sqlite3.connect('sentiment_analysis.db')
    cursor = conn.cursor()

    
    #Creating the SQL Tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY, 
        title TEXT, 
        url TEXT, 
        content TEXT, 
        sentiment TEXT, 
        probability REAL, 
        related_companies TEXT, 
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    #Test
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_sentiments (
        date DATE, 
        stock_symbol TEXT, 
        positive_count INTEGER DEFAULT 0, 
        negative_count INTEGER DEFAULT 0, 
        neutral_count INTEGER DEFAULT 0, 
        latest_sentiment TEXT, 
        latest_probability REAL, 
        PRIMARY KEY (date, stock_symbol)
    )
    ''')

    conn.commit()

    print("Deleting Old News (2 Days old)")
    delete_old_news(cursor=cursor, conn=conn)
    # Find all <a> tags with the 'data-p' attribute
    news_items = soup.find_all('a', attrs={'data-p': True})

    for item in news_items:
        news_url = item['href']  # The URL of the news item
        data_raw = item.get('data-p', '')  # Additional text provided in the data-p attribute, with a default if not present
        data_p = str(data_raw)
        title = item.get_text(strip=True)  # The text content of the <a> tag, which is the title of the news item
        text = f"Title: {title}, Content:  {data_p}"

        related_companies = find_related_articles(title=title, data_p=data_p)
        #print(related_companies)
        sentiment, probability = estimate_sentiment(text)
        
        # Print out if there are related companies
        if len(related_companies) != 0:
            if "http" in news_url:
                print(f"Related Companies: {related_companies}")
                print(f"Title: {title}")
                print(f"URL: {news_url}")
                print(f"Data: {data_p}")
                #print(type(data_p))
                print("---------")
                print(sentiment, probability)
                print("-+-+-+-+-+-+-+-+-+-+-+-\n")

        insert_news_update_sentiment(title=title, 
                                    url=news_url, 
                                    data_p=data_p, 
                                    sentiment=sentiment,
                                    probability=probability,
                                    related_companies=related_companies, 
                                    cursor=cursor, 
                                    conn=conn)
    


    print("\n\n\n\n\nScraping and processing logic executed!!\n\n\n\n\n")
    conn.close()

if __name__ == "__main__":
    main()
