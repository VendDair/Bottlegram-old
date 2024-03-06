from flask import Flask, json, jsonify, request, session
from flask_session import Session
import uuid
from flask_cors import CORS, cross_origin
import sqlite3 as sql
from time import sleep


app = Flask(__name__)
app.secret_key = "ENTER_YOUR_KEY"
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

CORS(app)

db: sql.Connection
cursor: sql.Cursor


def get_name(uuid: str):
    cursor.execute("""
    SELECT name
    FROM names
    WHERE uuid = ?
    """, (uuid,))
    return cursor.fetchone()[0]

def name_not_exists(name: str):
    cursor.execute("""
    SELECT name
    FROM names
    WHERE name = ?
    """, (name,))
    row = cursor.fetchone()
    if row:
        return False
    return True

@app.post("/init")
def init():
    global db
    global cursor
    try:
        db = sql.connect("posts.db", check_same_thread=False)
        cursor = db.cursor()
        sleep(1)
        return "200"
    except Exception as e:
        print(e)
        return "500"



@cross_origin
@app.post("/delete_post")
def delete_post():
    # Accept {id: integer}
    id = request.json["id"]
    cursor.execute("""
    DELETE FROM posts
    WHERE id = ?
    """, (id,))
    cursor.execute("""
    DELETE FROM comments
    WHERE id = ?
    """, (id,))
    db.commit()
    return "200"

@cross_origin
@app.post("/delete_comment")
def delete_comment():
    # Accept {name: string, text: string, id_p: integer}
    name = request.json["name"]
    text = request.json["text"]
    id_p = request.json["id_p"]
    cursor.execute("""
    DELETE FROM comments
    WHERE name = ? AND text = ? AND id_p = ?

    """, (name, text, id_p,))
    db.commit()
    return "200"


@cross_origin
@app.post("/get_names")
def get_names():
    # Accept {uuid: string}
    # Return {names: list}
    uuid = request.json["uuid"]
    name = get_name(uuid)
    print(name)
    
    cursor.execute("""
    SELECT *
    FROM messages
    WHERE name = ?;
    """, (name,))
    data = cursor.fetchall()

    names = []
    prev_name = ""

    for message in data:
        name = message[-1]
        if prev_name != name and name not in names:
            prev_name = name
            names.append(name)
    return jsonify(names=names)

@cross_origin
@app.post("/get_messages")
def get_messages():
    # Accept {uuid: string, sender: string}
    # Return {sender: string, text: string}
    uuid = request.json["uuid"]
    sender = request.json["sender"]
    name = get_name(uuid)
    cursor.execute("""
    SELECT *
    FROM messages
    WHERE name = ? AND sender = ?
    """, (name, sender,))

    data = cursor.fetchall()
    print(data)
    sender = []
    text = []
    for message in data:
        sender.append(message[-1])
        text.append(message[0])
    return jsonify({"sender": sender, "text": text})



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
    # Accept {text: string, name: string, uuid: string}
    text = request.json["text"]
    name = request.json["name"]
    uuid = request.json["uuid"]

    if name_not_exists(name):
        return "name not found"


    sender = get_name(uuid)
    print(sender)
    cursor.execute("""
    INSERT INTO messages (text, name, sender)
    VALUES (?, ?, ?)
    """, (text, name, sender,))
    db.commit()
    return "200"

@cross_origin
@app.post("/check_name")
def check_name():
    # Accept {uuid: string}
    # Return {name: string}
    uuid = request.json["uuid"]
    print(uuid)
    cursor.execute("SELECT name FROM names WHERE uuid = ?", (uuid,))
    row = cursor.fetchone()
    print(row)
    if row:
        return jsonify({"name": row[0]})
    return "500"

@cross_origin
@app.post("/set_name")
def set_name():
    try:
        name = request.json["name"]
        uuid = request.json["uuid"]
        print(name)
        cursor.execute("""
            INSERT INTO names (name, uuid) VALUES (?, ?)
        """, (name, uuid,))
        db.commit()
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

        print(text)
        print(name)
        print(type(id))

        cursor.execute("""
            INSERT INTO comments (text, id, name)
            VALUES (?, ?, ?)
        """, (text, str(id), name))
        db.commit()
        return "200"
    except Exception as e:
        print(e)
        return "500"


@app.post("/get_comments")
def get_comments():
    # Accept {id: number}
    id = request.json["id"]
    cursor.execute(f"""
        SELECT *
        FROM comments
        WHERE id = ?
    """, (id,))
    data = cursor.fetchall()
    print(data)
    return jsonify(data=data)

@app.post("/get_posts")
def get_posts():
    try:
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
        return jsonify(titles=titles, descriptions=descriptions, base64=base64, ids=ids, names=names)
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


init()
