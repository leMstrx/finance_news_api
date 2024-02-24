from flask import Flask, request, jsonify
import datetime 
import sqlite3
import secrets
import functools

#Creating the Flask App
app = Flask("Finance_News_API")

#Establishing a Connection to my Database
def get_db_connection():
    conn = sqlite3.connect('sentiment_analysis.db')
    conn.row_factory = sqlite3.Row
    return conn


"""
ALL API-Key RELATED STUFF
"""
def generate_api_key():
    return secrets.token_urlsafe(16) #Generates a secure, random URL-safe text

def add_api_key_to_db(key, owner):
    conn = sqlite3.connect('sentiment_analysis.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO api_keys (key, owner, creation_date) VALUES (?, ?, ?)',
                (key, owner, datetime.datetime.now()))
    conn.commit()
    conn.close()

def require_api_key(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if 'API-Key' not in request.headers: 
            return jsonify({"error": "API key is missing"}), 403
        
        api_key = request.headers['API-Key']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM api_keys WHERE key = ?", (api_key,))
        key_exists = cur.fetchone()
        conn.close()

        if key_exists:
            return f(*args, **kwargs)
        else: 
            return jsonify({"error": "Invalid Api Key"}), 403
        
    return decorated_function


@app.route('/')
#Basic Homepage 
def home():
    return "Welcome to the Finance News API"

#End point to fetch all news
@app.route('/news/all')
@require_api_key
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
@require_api_key
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