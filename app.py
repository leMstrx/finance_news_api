from flask import Flask, request, jsonify
import datetime 
import sqlite3
import secrets
import functools
import sys
import click
from flask.cli import with_appcontext

#Creating the Flask App
app = Flask("Finance_News_API")

#Establishing a Connection to my Database
def get_db_connection():
    conn = sqlite3.connect('sentiment_analysis.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.cli.command('create-api-key')
@with_appcontext
@click.argument('owner')
def create_api_key(owner):
    """Generate a new API key for the specified owner"""
    existing_key = check_owner_has_key(owner)
    if existing_key: 
        print(f"Owner already has an API key: {existing_key['key']}")
    else: 
        key = generate_api_key()
        add_api_key_to_db(key, owner)
        print(f"Generated new API key for: {owner}: {key}")


"""
ALL API-Key RELATED STUFF
"""
def generate_api_key():
    return secrets.token_urlsafe(16) #Generates a secure, random URL-safe text

def add_api_key_to_db(key, owner):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO api_keys (key, owner, creation_date) VALUES (?, ?, ?)',
                (key, owner, datetime.datetime.now()))
    conn.commit()
    conn.close()

def check_owner_has_key(owner):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM api_keys WHERE owner = ?', (owner,))
    key_info = cur.fetchone()
    conn.close()
    return key_info



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

    cur.execute('SELECT * FROM news WHERE related_companies LIKE ? ORDER BY id DESC', ('%' + symbol + '%',))
    news_items = cur.fetchall()
    
    news_list = [dict(ix) for ix in news_items]
    
    conn.close()
    return jsonify(news_list)


if __name__ == "__main__":
    app.run(debug=True)