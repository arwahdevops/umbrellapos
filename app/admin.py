from flask import Flask, render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def main_index():
    return render_template('layout.html')