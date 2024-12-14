import sqlite3


conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS products")

cursor.execute('''CREATE TABLE IF NOT EXISTS products 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    description VARCHAR(255),
    price INTEGER,
    img VARCHAR(200))''')


products = [('Apple iPhone 16 Pro Max 256GB White Titanium', 'телефон', 60892, 'product1.jpg'),
            ('Galaxy S24 Ultra 12/256GB Titanium Gray', 'телефон', 49599, 'product2.jpg'),
            ('Xiaomi 14 Ultra 16/512Gb White', 'телефон', 52999, 'product3.jpg'),
            ('ASUS TUF Gaming F15', 'ноутбук', 53999, 'product4.jpg'),
            ('Apple MacBook Pro 14 M4 16/1TB Space Gray', 'ноутбук', 99999, 'product5.jpg'),
            ('ASUS ROG Strix Scar 17', 'ноутбук', 169594, 'product6.jpg'),
            ('Apple iPad Pro 12.9" M2 Wi-Fi 1TB Space Gray', 'планшет', 66999, 'product7.jpg'),
            ('Samsung Galaxy Tab S10 Ultra 5G 12/512Gb Moonstone Gray', 'планшет', 66999, 'product8.jpg' ),
            ('Apple iPad 10.9'' (10 Gen) WiFi 64GB Blue', 'планшет', 16999, 'product9.jpg')]

for product in products:
        cursor.execute("INSERT INTO products (name, description, price, img) VALUES (?, ?, ?, ?)", product)

conn.commit()


products = cursor.execute("SELECT * FROM products").fetchall()
conn.close()

for product in products:
    print(product)