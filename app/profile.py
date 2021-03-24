from flask import Flask, render_template, Blueprint, session, redirect, url_for
from .extensions import mysql
profile = Blueprint('profile', __name__)

@profile.route('/profile')
def profile_index():
    judul = "Profile"
    return render_template('user_profile.html', judul=judul)