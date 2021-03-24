from flask import Flask, render_template, Blueprint, session, redirect, url_for
from .extensions import mysql
supplier = Blueprint('supplier', __name__)

@supplier.route('/supplier')
def supplier_index():
    judul = "Supplier"
    return render_template('supplier.html', judul=judul)

@supplier.route('/supplier/order')
def supplier_order():
    judul = "Supplier Order"
    return render_template('supplier_order.html', judul=judul)