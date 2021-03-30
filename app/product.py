from flask import Flask, render_template, Blueprint, session, redirect, url_for, request
from werkzeug.utils import secure_filename
from .extensions import mysql
product = Blueprint('product', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@product.route('/product')
def product_index():
    try:
        user = session['name']
        judul = "Produk"
        cur = mysql.connection.cursor()
        cur.execute("SELECT \
	product.id, \
	product.product_code, \
	product.product_name, \
	product_category.jenis, \
	product_category.satuan, \
	product.price_sell, \
	product.stock, \
	product.disc \
FROM \
	product \
	INNER JOIN \
	product_category \
	ON  \
		product.category = product_category.id")
        data = cur.fetchall()
        cur.close()
        return render_template('/product/product.html', menu='Product', submenu='Data Product', judul=judul, product=data)
    except:
        return redirect(url_for("login.login_index"))

@product.route('/add_product', methods=['GET','POST'])
def add_product():
    if request.method == 'GET':
        judul = "Tambah Produk"
        user = session['name']
        #get product category
        cur = mysql.connection.cursor()
        cur.execute("select * from product_category")
        prod_cat = cur.fetchall()
        cur.close()
        return render_template('/product/add_product.html', judul=judul, data=prod_cat)
    else:
        #insert products
        product_code = request.form['product_code']
        product_name = request.form['product_name']
        category = request.form['category']
        price_sell = request.form['price_sell']
        disc = request.form['disc']
        stock = request.form['stock']
        product_desc = request.form['product_desc']
        qr_bar_code = request.form['qr_bar_code']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO product (product_code,product_name,category,price_sell,stock,disc,product_desc,qr_bar_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(product_code,product_name,category,price_sell,stock,disc,product_desc,qr_bar_code))
        mysql.connection.commit()

        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

        return redirect(url_for("product.add_product"))

@product.route('/category')
def product_category():
    user = session['name']
    judul = "Kategori Produk"
    cur = mysql.connection.cursor()
    cur.execute("select * from product_category")
    data = cur.fetchall()
    cur.close()
    return render_template('/product/product_category.html', menu='Product', submenu='Product Category', judul=judul, category=data)

@product.route('/add_category', methods=['GET','POST'])
def add_category():
    if request.method == 'GET':
        judul = "Tambah Kategori"
        user = session['name']
        return render_template('/product/add_product_category.html', judul=judul)
    else:
        jenis = request.form['jenis']
        satuan = request.form['satuan']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO product_category (jenis,satuan) VALUES (%s,%s)",(jenis,satuan))
        mysql.connection.commit()
        return redirect(url_for("product.add_category"))