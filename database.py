import sqlite3


conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS products")

cursor.execute('''CREATE TABLE IF NOT EXISTS products 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    description VARCHAR(255),
    price INTEGER,
    image VARCHAR(200))''')


products = [('Apple iPhone 16 Pro Max 256GB White Titanium', 'телефон', 60892, 'product1.jpg'),
            ('Galaxy S24 Ultra 12/256GB Titanium Gray', 'телефон', 49599, 'product2.jpg'),
            ('Xiaomi 14 Ultra 16/512Gb White', 'телефон', 52999, 'product3.jpg'),
            ('ASUS TUF Gaming F15', 'ноутбук', 53999, 'product4.jpg'),
            ('Apple MacBook Pro 14 M4 16/1TB Space Gray', 'ноутбук', 99999, 'product5.jpg'),
            ('ASUS ROG Strix Scar 17', 'ноутбук', 169594, 'product6.jpg')]

for product in products:
        cursor.execute("INSERT INTO products (name, description, price, image) VALUES (?, ?, ?, ?)", product)

conn.commit()

    # Получение данных
products = cursor.execute("SELECT * FROM products").fetchall()
conn.close()

for product in products:
    print(product)