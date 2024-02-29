from sys import exception
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import sqlite3 as sql


app = Flask(__name__)

CORS(app)

@cross_origin
@app.post("/new_comment")
def new_comment():
    #Accept {text: string, id: number, name: string}
    try:
        text = request.json["text"]
        id = request.json["id"]
        name = request.json["name"]
        db = sql.connect("posts.db")
        cursor = db.cursor()
        cursor.execute("""
        INSERT INTO comments (text, id, name)
        VALUES (?, ?, ?)
        """, (text, id[0], name,))
        db.commit()
        cursor.close()
        db.close()
        return "200"
    except Exception as e:
        print(e)
        return "500"

@app.post("/get_comments")
def get_comments():
    # Accept {id: number}
    try:
        id = request.json["id"][0]
        print(id)
        db = sql.connect("posts.db")
        cursor = db.cursor()

        cursor.execute(f"""
            SELECT id, text, name
            FROM comments
            WHERE id = ?
        """, (id, ))
        data = cursor.fetchall()
        return jsonify(data=data)
    except:
        return "500"

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
        cursor.execute("SELECT id FROM posts")
        ids = cursor.fetchall()
        return jsonify(titles=titles, descriptions=descriptions, base64=base64, ids=ids)
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
