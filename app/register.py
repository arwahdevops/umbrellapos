from flask import Flask, render_template, Blueprint, request, session, redirect, url_for
import bcrypt
from .extensions import mysql
register = Blueprint('register', __name__)

@register.route('/register', methods=['GET','POST'])
def register_index():
    if request.method == 'GET':
        return render_template('/user/register.html')
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        user_level = 1
        user_status = 0

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO login (name,email,password,user_levels,status) VALUES (%s,%s,%s,%s,%s)",(name,email,hash_password,user_level,user_status))
        mysql.connection.commit()
        session['name'] = name
        session['email'] = email
        return redirect(url_for("login.login_index"))