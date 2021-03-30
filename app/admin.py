from flask import Flask, render_template, Blueprint, session, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/dashboard')
def main_index():
    try:
        user = session['name']
        judul = "Dashboard"
        return render_template('layout.html', menu='Dashboard', submenu='Dashboard', judul=judul)
    except:
        return redirect(url_for("login.login_index"))
    