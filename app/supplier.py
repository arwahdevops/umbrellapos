from flask import Flask, render_template, Blueprint, session, redirect, url_for, request
from .extensions import mysql, MySQLdb
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

@supplier.route('/supplier/edit/<string:id>', methods=['GET','POST'])
def edit_supplier(id):
    if request.method == 'GET':
        judul = "Edit Supplier"

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM suppliers WHERE id=%s", (id))
        data = cur.fetchall()
        cur.close()
        return render_template('/supplier/edit_supplier.html', judul=judul, supplier=data[0])
    else:
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        city = request.form['city']
        address = request.form['address']
        
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("""
                    UPDATE suppliers 
                    SET name=%s,
                        phone=%s,
                        email=%s,
                        city=%s,
                        address=%s 
                    WHERE id=%s
                    """,(name,phone,email,city,address,id))
        mysql.connection.commit()

        return redirect(url_for("supplier.supplier_index"))

@supplier.route('/supplier/delete/<string:id>', methods=['GET','POST'])
def delete_supplier(id):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("DELETE FROM suppliers WHERE id={0}".format(id))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for("supplier.supplier_index"))
