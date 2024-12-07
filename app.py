from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()
    products = cursor.execute("SELECT * FROM products").fetchall()
    connection.close()
    print(products)
    return render_template('products.html', products=products)


app.run(debug=True)
