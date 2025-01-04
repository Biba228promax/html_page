import sqlite3

conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS products")

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    description VARCHAR(255),
    price INTEGER,
    img VARCHAR(200),
    display VARCHAR(255),
    os VARCHAR(255),
    screen VARCHAR(255),
    battery VARCHAR(255),
    processor VARCHAR(255),
    camera VARCHAR(255)
)''')

products = [
    ('Apple iPhone 16 Pro Max 256GB White Titanium', 'телефон', 60892, 'product1.jpg', '6.7" OLED', 'iOS', '2532 x 1170', '4373 mAh', 'A16 Bionic', '12 MP'),
    ('Galaxy S24 Ultra 12/256GB Titanium Gray', 'телефон', 49599, 'product2.jpg', '6.8" AMOLED', 'Android', '3200 x 1440', '5000 mAh', 'Exynos 2200', '108 MP'),
    ('Xiaomi 14 Ultra 16/512Gb White', 'телефон', 52999, 'product3.jpg', '6.81" AMOLED', 'Android', '3200 x 1440', '5000 mAh', 'Snapdragon 8 Gen 1', '50 MP'),
    ('ASUS TUF Gaming F15', 'ноутбук', 53999, 'product4.jpg', '15.6" IPS', 'Windows', '1920 x 1080', '90 Wh', 'Intel Core i7', '720p HD'),
    ('Apple MacBook Pro 14 M4 16/1TB Space Gray', 'ноутбук', 99999, 'product5.jpg', '14.2" Retina', 'macOS', '3024 x 1964', '100 Wh', 'Apple M4', '1080p HD'),
    ('ASUS ROG Strix Scar 17', 'ноутбук', 169594, 'product6.jpg', '17.3" IPS', 'Windows', '2560 x 1440', '90 Wh', 'AMD Ryzen 9', '720p HD'),
    ('Apple iPad Pro 12.9" M2 Wi-Fi 1TB Space Gray', 'планшет', 66999, 'product7.jpg', '12.9" Liquid Retina', 'iPadOS', '2732 x 2048', '9720 mAh', 'Apple M2', '12 MP'),
    ('Samsung Galaxy Tab S10 Ultra 5G 12/512Gb Moonstone Gray', 'планшет', 66999, 'product8.jpg', '12.4" Super AMOLED', 'Android', '2800 x 1752', '10090 mAh', 'Snapdragon 8 Gen 1', '13 MP'),
    ('Apple iPad 10.9'' (10 Gen) WiFi 64GB Blue', 'планшет', 16999, 'product9.jpg', '10.9" Liquid Retina', 'iPadOS', '2360 x 1640', '7606 mAh', 'A14 Bionic', '12 MP')
]

for product in products:
    cursor.execute("INSERT INTO products (name, description, price, img, display, os, screen, battery, processor, camera) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", product)

conn.commit()

products = cursor.execute("SELECT * FROM products").fetchall()
conn.close()

for product in products:
    print(product)
