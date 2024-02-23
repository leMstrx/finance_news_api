from flask import Flask, jsonify
import datetime 
import sqlite3

#Creating the Flask App
app = Flask("Finance_News_API")

#Establishing a Connection to my Database
def get_db_connection():
    conn = sqlite3.connect('sentiment_analysis.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
#Basic Homepage 
def home():
    return "Welcome to the Finance News API"

#End point to fetch all news
@app.route('/news/all')
def get_all_news():
    conn = get_db_connection() #Connecting to DB
    cur = conn.cursor() #Making Edits available
    cur.execute('SELECT * FROM news ORDER BY id ASC')
    news_items = cur.fetchall()

    #Convert the result to a list of dicts, which can be easily turned into JSON
    news_list = [dict(ix) for ix in news_items]

    conn.close()    #Closing DB Connection to avoid data leaks
    return jsonify(news_list)

#End point to Fetch News for a specific symbol
@app.route('/news/<symbol>')
def get_news_for_symbol(symbol:str):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM news WHERE related_companies LIKE ? ORDER BY id ASC', ('%' + symbol + '%',))
    news_items = cur.fetchall()
    
    news_list = [dict(ix) for ix in news_items]
    
    conn.close()
    return jsonify(news_list)


if __name__ == "__main__":
    app.run(debug=True)