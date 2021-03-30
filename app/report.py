from flask import Flask, render_template, Blueprint, session, redirect, url_for
from .extensions import mysql
report = Blueprint('report', __name__)

@report.route('/pendapatan')
def report_pemasukan():
    judul = "Pendapatan"
    return render_template('/report/pendapatan.html', menu='Report', submenu='Pendapatan', judul=judul)

@report.route('/report/pengeluaran')
def report_pengeluaran():
    judul = "Pengeluaran"
    return render_template('/report/pengeluaran.html', menu='Report', submenu='Pengeluaran', judul=judul)