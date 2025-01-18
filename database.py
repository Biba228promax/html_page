import os
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Необходимо для использования flash сообщений
app.config['UPLOAD_FOLDER'] = 'C:/Users/LOGIKA/PycharmProjects/html_page/static/img'


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
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        img = request.files.get('img')
        display = request.form.get('display')
        operating_system = request.form.get('operating_system')
        screen = request.form.get('screen')
        battery = request.form.get('battery')
        processor = request.form.get('processor')
        camera = request.form.get('camera')

        if not all([name, description, price, img, display, operating_system, screen, battery, processor, camera]):
            flash("Пожалуйста, заполните все поля, включая изображение.")
        else:
            img_filename = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)

            # Создание конечной папки, если она не существует
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            try:
                img.save(img_filename)
                flash("Файл успешно сохранен.")
                connection.execute('''INSERT INTO products (name, description, price, img, display, operating_system, screen, battery, processor, camera) 
                                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                   (name, description, price, img.filename, display, operating_system, screen, battery, processor, camera))
                connection.commit()
                flash("Продукт успешно добавлен.")
            except Exception as e:
                flash(f"Ошибка при загрузке файла: {e}")

    products = connection.execute('SELECT * FROM products').fetchall()
    connection.close()
    return render_template('admin.html', products=products)


@app.route('/admin/delete', methods=['POST'])
def delete_product():
    connection = get_db_connection()
    product_id = request.form['product_id']
    connection.execute("DELETE FROM products WHERE id = ?", (product_id,))
    connection.commit()
    connection.close()
    flash("Продукт успешно удален.")
    return redirect(url_for('admin'))

@app.route('/purchase_info')
def purchase_info():
    return render_template('purchase_info.html')

@app.route('/process_purchase', methods=['POST'])
def process_purchase():
    fio = request.form.get('fio')
    email = request.form.get('email')
    address = request.form.get('address')
    phone = request.form.get('phone')

    # Здесь можно добавить код для обработки данных, например, сохранить их в базу данных или отправить по email

    flash("Покупка успешно оформлена!")
    return redirect(url_for('index'))


if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
