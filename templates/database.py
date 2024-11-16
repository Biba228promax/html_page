import sqlite3

connection = sqlite3.connect("database.sqlite")
cursor = connection.cursor()

request = ("CREATE TABLE IF NOT EXISTS products"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "description VARCHAR(255),"
           "price INTEGER)")
cursor.execute(request)

insert_request = ("INSERT INTO products"
                  "(name, description, price) VALUES (?, ?, ?)")
cursor.execute(insert_request, ("телефон", "Apple iPhone 16 Pro Max 256GB White Titanium", 60892))
cursor.execute(insert_request, ("телефон", "Galaxy S24 Ultra 12/256GB Titanium Gray", 49599))
cursor.execute(insert_request, ("телефон", "Xiaomi 14 Ultra 16/512Gb White", 52999))
cursor.execute(insert_request, ("ноутбук", "ASUS TUF Gaming F15", 53999))
cursor.execute(insert_request, ("ноутбук", "Apple MacBook Pro 14 M4 16/1TB Space Gray", 99999))
cursor.execute(insert_request, ("ноутбук", "ASUS ROG Strix Scar 17 AMD Ryzen 9 7945HX NVIDIA GeForce RTX 4090, 16 ГБ GDDR6 Space Gray 32/2TB", 169594))




connection.commit()

text = cursor.execute("SELECT * FROM products")
for line in text.fetchall():
    print(line)