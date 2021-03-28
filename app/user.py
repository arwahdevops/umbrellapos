from flask import Flask, render_template, Blueprint, session, redirect, url_for
from .extensions import mysql
user = Blueprint('user', __name__)

@user.route('/user')
def user_index():
    judul = "Data User"
    return render_template('/user/user.html', judul=judul)