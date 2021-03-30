from flask import Flask, render_template, Blueprint
from .extensions import mysql
forgot = Blueprint('forgot', __name__)

@forgot.route('/forgot')
def forgot_index():
    
    return render_template('/user/forgot_password.html')