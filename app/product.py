from flask import Flask, render_template, Blueprint
from .extensions import mysql
product = Blueprint('product', __name__)

@product.route('/product')
def product_index():
    judul = "Produk"
    cur = mysql.connection.cursor()
    cur.execute("select * from product")
    data = cur.fetchall()
    cur.close()
    return render_template('product.html', judul=judul, product=data)