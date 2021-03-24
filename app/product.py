from flask import Flask, render_template, Blueprint, session, redirect, url_for
from .extensions import mysql
product = Blueprint('product', __name__)

@product.route('/product')
def product_index():
    try:
        user = session['name']
        judul = "Produk"
        cur = mysql.connection.cursor()
        cur.execute("select * from product")
        data = cur.fetchall()
        cur.close()
        return render_template('product.html', judul=judul, product=data)
    except:
        return redirect(url_for("login.login_index"))

@product.route('/category')
def product_category():
    judul = "Kategori"
    return render_template('category_products.html', judul=judul)