from flask import Flask, render_template, Blueprint, session, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/dashboard')
def main_index():
    try:
        user = session['name']
        return render_template('layout.html')
    except:
        return redirect(url_for("login.login_index"))
    