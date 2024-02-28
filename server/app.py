from sys import exception
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import sqlite3 as sql


app = Flask(__name__)

CORS(app)

@app.post("/get_posts")
def get_posts():
    try:
        db = sql.connect("posts.db")
        cursor = db.cursor()
        cursor.execute("SELECT title from posts")
        titles = cursor.fetchall()
        cursor.execute("SELECT description from posts")
        descriptions = cursor.fetchall()
        cursor.execute("SELECT base64 from posts")
        base64 = cursor.fetchall()
        return jsonify(titles=titles, descriptions=descriptions, base64=base64)
    except:
        return "500"

@cross_origin
@app.post("/new_post")
def new_post():
    # {"title": "title", "description": "desc", "base64": "encoded image in base64"}
    try: 
        title = request.json["title"]
        description = request.json["description"]
        base64 = request.json["base64"]
        db = sql.connect("posts.db")
        print(title)
        cursor = db.cursor()
        cursor.execute("INSERT INTO posts (title, description, base64) VALUES (?, ?, ?)", (title, description, base64))
        db.commit()
        cursor.close()
        db.close()
        return "200"
    except sql.OperationalError:
        return "500"
