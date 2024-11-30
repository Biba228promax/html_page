import sqlite3


conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

    # Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
     name VARCHAR(255),
     description VARCHAR(255),
     price INTEGER)
    ''')

    # Вставка данных
products = [
    ("телефон", "Apple iPhone 16 Pro Max 256GB White Titanium", 60892),
    ("телефон", "Galaxy S24 Ultra 12/256GB Titanium Gray", 49599),
    ("телефон", "Xiaomi 14 Ultra 16/512Gb White", 52999),
    ("ноутбук", "ASUS TUF Gaming F15", 53999),
    ("ноутбук", "Apple MacBook Pro 14 M4 16/1TB Space Gray", 99999),
    ("ноутбук", "ASUS ROG Strix Scar 17 AMD Ryzen 9 7945HX NVIDIA GeForce RTX 4090, 16 ГБ GDDR6 Space Gray 32/2TB", 169594)]

for product in products:
        cursor.execute("INSERT INTO products (name, description, price) VALUES (?, ?, ?)", product)

conn.commit()

    # Получение данных
products = cursor.execute("SELECT * FROM products").fetchall()
conn.close()

for product in products:
    print(product)