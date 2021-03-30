from flask import Flask, render_template, Blueprint, session, redirect, url_for, request
from .extensions import mysql
supplier = Blueprint('supplier', __name__)

@supplier.route('/supplier')
def supplier_index():
    try:
        user = session['name']
        judul = "Supplier"
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM suppliers")
        data = cur.fetchall()
        cur.close()
        return render_template('/supplier/supplier.html', menu='Supplier', submenu='Data Supplier', judul=judul, suppliers=data)
    except:
        return redirect(url_for("login.login_index"))

@supplier.route('/supplier/order')
def supplier_order():
    judul = "Supplier Order"
    return render_template('/supplier/supplier_order.html', menu='Supplier', submenu='Supplier Order', judul=judul)

@supplier.route('/add_supplier', methods=['GET','POST'])
def add_supplier():
    if request.method == 'GET':
        judul = "Tambah Supplier"
        return render_template('/supplier/add_supplier.html', judul=judul)
    else:
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        city = request.form['city']
        address = request.form['address']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO suppliers (name,phone,email,city,address) VALUES (%s,%s,%s,%s,%s)",(name,phone,email,city,address))
        mysql.connection.commit()

        return redirect(url_for("supplier.add_supplier"))