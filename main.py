import sqlite3
from flask import Flask , request, render_template, url_for,\
    redirect, escape, session, flash, jsonify

from db import sql_db as db

from auth import bp_auth

# virtualenv venv - загрузка виртуальной среды 
# source venv/bin/activate - активируем виртуальную среду 
# pip install flask - загрузка фласка 
# pip необходим для подгрузки дополнительных модулей 
# любая ОС принимает 2 вида аргументов с 1 (-) и 2(-)

# export FLASK_APP=main.py
# flask run

app = Flask(__name__)
app.secret_key = "one" 
# name - название модуля, такое же как имя файла 

app.register_blueprint(bp_auth)

db.execute_sql_file("db/SQL/create_db.sql")

@app.route("/posts/<login>")
@app.route("/posts", methods=["POST", "GET"])
def posts(login=None):
    if request.method == "GET":
        get_login = f"SELECT id FROM users WHERE login = '{login}'"
        request_id = db.query(get_login, assoc=True)
        user_id = request_id[0]["id"]
        get_post = f"SELECT * FROM posts WHERE user = {user_id} ORDER BY created ASC"
        # ORDER BY  - в какаом порядке  , created - поле , ASC - наоборот 
        request_post = db.query(get_post, True)
        return jsonify(request_post)
        # jsonify - переводит массив в json 

        # return render_template("posts.html")
    elif request.method == "POST":
        get_id = request.form["id"]
        get_text = request.form["post_text"]
        add_values = f"INSERT INTO posts(user, text) VALUES ('{get_id}', '{get_text}')"
        user_id = db.insert(add_values)
        add_post = f"SELECT u.display_name , p.text , p.updated as date FROM posts as p \
            INNER JOIN users as u ON u.id = p.user WHERE p.id = {user_id}"
            # мы берем данные login  - в users , text - в posts 
            # as переименовывает данные для текущего запроса 
        # INNER JOIN  - позволяет дополнительно прикрепить 2 таблицу 
        post = db.query(add_post, True)
        responce = {
            "success":True,
            "result": []
        }
       
        responce["result"].append(post[0])
        # [0] - берем первый  SELECT - это u.display_name
        return jsonify(responce)
        

@app.route('/')
def index():
    if "id" in session:
        return redirect(url_for("main"))
    return render_template("index.html", title="Главная")

with app.test_request_context():
    print(url_for("index"))

@app.route('/main', methods=['GET'])
def main():
    if "id" in session:
        id_session = escape(session["id"])
        get_session_data = f"SELECT * FROM users WHERE id = {id_session}"
        callUser = db.query(get_session_data, assoc=True)
        
        return render_template(
            "main.html",

            name=callUser[0]["display_name"], 
            born=callUser[0]["bithday"],
            title= callUser[0]["display_name"],
            id= callUser[0]["id"]
        )
    return redirect(url_for("index"))

# куки файлы и фласк 

# flask upload files
# придумать модель постинга текста (id , username, text, URL , )
