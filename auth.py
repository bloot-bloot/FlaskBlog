from flask import Blueprint , request, session, render_template, redirect, url_for, flash

from db import sql_db as db 

bp_auth = Blueprint("authorization", __name__)

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    # почему нельзя убрать проверку GET', 'POST' ?
    if request.method == "GET":
        print(request.form)
        return render_template("login.html", title="GET Запрос")
    elif request.method == "POST":
        print(request.form)
        get_login = request.form["login"]
        get_password = request.form["password"]
        cur = f"SELECT login, password, id FROM users WHERE login = '{get_login}' "
        result = db.query(cur, assoc=True)     
        if result[0]["login"] == get_login and result[0]["password"] == get_password:
            session["id"] = result[0]["id"]
            
            # не удаляется сообщение после обновления страницы 
            return redirect(url_for("main"))

    flash("Не верный логин или пароль")
    return render_template("login.html")

@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html", title="GET Запрос")
    elif request.method == "POST":
        # print(url_for("register"))
        # print(request.form) -- появляются баги от print
        login = request.form["login"]
        password = request.form["password"]
        mail = request.form["mail"]
        bithday = request.form["bithday"]
        display_name = request.form["display_name"]
        add_user = f"INSERT INTO users (login, password, mail, bithday, display_name )\
                  VALUES ('{login}','{password}','{mail}', '{bithday}','{display_name}')"
        db.query(add_user)
        get_id = f"SELECT id FROM users WHERE login='{login}'"
        new_user = db.query(get_id, assoc=True)
        session["id"] = new_user[0]["id"]
        # TODO: result == [], чтобы проверить зарегистрирован ли пользователь 
        return redirect(url_for("main"))

register
@bp_auth.route('/logout', methods=['GET'])
def logout():
    session.pop("id", None)
    return redirect(url_for("index"))

