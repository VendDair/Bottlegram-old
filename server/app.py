from flask import Flask, json, jsonify, request
from flask_cors import CORS, cross_origin
import sqlite3 as sql
from time import sleep


app = Flask(__name__)

CORS(app)

db: sql.Connection
cursor: sql.Cursor

@app.post("/init")
def init():
    global db
    global cursor
    try:
        db = sql.connect("posts.db")
        cursor = db.cursor()
        sleep(1)
        return "200"
    except Exception as e:
        print(e)
        return "500"

@app.post("/test")
def test():
    cursor.execute("""
    SELECT *
    FROM messages
    """)
    print(cursor.fetchall())
    return "200"


@cross_origin
@app.post("/new_message")
def new_message():
    # Accept {text: string, name: string}
    text = request.json["text"]
    name = request.json["name"]
    sender = request.json["sender"]
    print(sender)
    #db = sql.connect("./posts.db")
    #cursor = db.cursor()
    cursor.execute("""
    INSERT INTO messages (text, name, sender)
    VALUES (?, ?, ?)
    """, (text, name, sender,))
    db.commit()
    #cursor.close()
    #db.close()
    return "200"

@cross_origin
@app.post("/set_name")
def set_name():
    # Accept {name: string}
    try:
        name = request.json["name"]
        print(name)
        #db = sql.connect("./posts.db")
        #cursor = db.cursor()
        cursor.execute("""
            INSERT INTO names (name) VALUES (?)
        """, (name,))
        db.commit()
        #cursor.close()
        #db.close()
        return "200"
    except Exception as e:
        print(e)
        return "500"

@cross_origin
@app.post("/new_comment")
def new_comment():
    #Accept {text: string, id: number, name: string}
    try:
        text = request.json["text"]
        id = request.json["id"]
        name = request.json["name"]
        #db = sql.connect("./posts.db")
        print(text)
        print(name)
        print(type(id))
        #cursor = db.cursor()
        cursor.execute("""
            INSERT INTO comments (text, id, name)
            VALUES (?, ?, ?)
        """, (text, str(id), name))
        db.commit()
        #cursor.close()
        #db.close()
        return "200"
    except Exception as e:
        print(e)
        return "500"


@app.post("/get_comments")
def get_comments():
    # Accept {id: number}
    id = request.json["id"]
    #db = sql.connect("./posts.db")
    #cursor = db.cursor()

    cursor.execute(f"""
        SELECT *
        FROM comments
        WHERE id = ?
    """, (id,))
    data = cursor.fetchall()
    print(data)
    return jsonify(data=data)

    #try:
    #    id = request.json["id"][0]
    #    id = str(id)
    #    print(id)
    #    db = sql.connect("posts.db")
    #    cursor = db.cursor()

    #    cursor.execute(f"""
    #        SELECT *
    #        FROM comments
    #        WHERE id = ?
    #    """, (id))
    #    data = cursor.fetchall()
    #    print(data)
    #    return jsonify(data=data)
    #except Exception as e:
    #    print(e)
    #    return "500"

@app.post("/get_posts")
def get_posts():
    try:
        #db = sql.connect("./posts.db")
        #cursor = db.cursor()
        cursor.execute("""
            SELECT *
            FROM posts
            ORDER BY id DESC
        """)
        data = cursor.fetchall()
        titles = []
        descriptions = []
        base64 = []
        ids = []
        names = []
        for post in data:
            titles.append(post[0])
            descriptions.append(post[1])
            base64.append(post[2])
            ids.append(post[3])
            names.append(post[4])
        #cursor.execute("SELECT title from posts")
        #titles = cursor.fetchall()
        #cursor.execute("SELECT description from posts")
        #descriptions = cursor.fetchall()
        #cursor.execute("SELECT base64 from posts")
        #base64 = cursor.fetchall()
        #cursor.execute("SELECT id FROM posts")
        #ids = cursor.fetchall()
        #cursor.execute("SELECT name FROM posts")
        #names = cursor.fetchall()
        return jsonify(titles=titles, descriptions=descriptions, base64=base64, ids=ids, names=names)
        #return jsonify(title=data[0], description=data[1], base64=data[2], ids=data[3], names=data[4])
    except:
        return "500"

@cross_origin
@app.post("/new_post")
def new_post():
    # {"title": "title", "description": "desc", "base64": "encoded image in base64", "name": string}
    try: 
        title = request.json["title"]
        description = request.json["description"]
        base64 = request.json["base64"]
        name = request.json["name"]
        #db = sql.connect("./posts.db")
        #cursor = db.cursor()
        cursor.execute("INSERT INTO posts (title, description, base64, name) VALUES (?, ?, ?, ?)", (title, description, base64, name,))
        db.commit()
        #cursor.close()
        #db.close()
        return "200"
    except:
        return "500"
