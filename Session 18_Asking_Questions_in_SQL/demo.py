import sqlite3
connection = sqlite3.connect("store.db")
cursor = connection.cursor()
cursor.execute("""
 CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        quantity INTEGER
    )
""")

connection.commit()

cursor.execute("""
    INSERT INTO products (name, price, quantity)
    VALUES (?, ?, ?)
""", ("Laptop", 55000, 10))

connection.commit()

cursor.execute("SELECT * FROM products")

products = cursor.fetchall()

for product in products:
    print(product)
    
connection.close()