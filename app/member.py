from flask import Flask, render_template, Blueprint, session, redirect, url_for
from .extensions import mysql
member = Blueprint('member', __name__)

@member.route('/member')
def member_index():
    judul = "Member"
    return render_template('member.html', judul=judul)