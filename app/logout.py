from flask import Flask, render_template, Blueprint, session, redirect, url_for
logout = Blueprint('logout', __name__)

@logout.route('/logout')
def logout_index():
    session.clear()
    return redirect(url_for("login.login_index"))