from flask import Flask, render_template, Blueprint, session, redirect, url_for
from .extensions import mysql
report = Blueprint('report', __name__)

@report.route('/pemasukan')
def report_pemasukan():
    judul = "Pemasukan"
    return render_template('pemasukan.html', judul=judul)

@report.route('/report/pengeluaran')
def report_pengeluaran():
    judul = "Pengeluaran"
    return render_template('pengeluaran.html', judul=judul)