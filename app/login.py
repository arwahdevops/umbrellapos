from flask import Flask, render_template, Blueprint, request, session, redirect, url_for
import bcrypt
from .extensions import mysql, MySQLdb
login = Blueprint('login', __name__)

@login.route('/', methods=['GET','POST'])
def login_index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM login WHERE email=%s",(email,))
        user = cur.fetchone()
        cur.close()

        if len(user) > 0:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['name'] = user['name']
                session['email'] = user['email']
                return redirect(url_for("main.main_index"))
            else:
                return "Error password or user not match"
    else:
        return render_template("login.html")