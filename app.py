from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("database.sqlite")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    connection = get_db_connection()
    products = connection.execute("SELECT * FROM products").fetchall()
    connection.close()
    return render_template('products.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    connection = get_db_connection()
    product = connection.execute("SELECT * FROM products WHERE id = ?", (product_id,)).fetchone()
    connection.close()
    return render_template('product_detail.html', product=product)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    connection = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        img = request.form['img']
        connection.execute('INSERT INTO products (name, description, price, img) VALUES (?, ?, ?, ?)', (name, description, price, img))
        connection.commit()
    products = connection.execute('SELECT * FROM products').fetchall()
    connection.close()
    return render_template('admin.html', products=products)

@app.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    connection = get_db_connection()
    connection.execute('DELETE FROM products WHERE id = ?', (product_id,))
    connection.commit()
    connection.close()
    return redirect(url_for('admin'))

if __name__ == "__main__":
    app.run(debug=True)
