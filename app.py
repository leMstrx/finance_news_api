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

#Example endpoint to fetch news
@app.route('/news')
def get_news():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM news ORDER BY id ASC')
    news_items = cur.fetchall()

    #Convert the result to a list of dicts, which can be easily turned into JSON
    news_list = [dict(ix) for ix in news_items]

    conn.close()
    return jsonify(news_list)


if __name__ == "__main__":
    app.run(debug=True)