import sqlite3

connection = sqlite3.connect("store.db")
cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS customers(
#     customer_id INTEGER PRIMARY KEY,
#     name TEXT, 
#     city TEXT
# )
# ''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS orders(
#     order_id INTEGER PRIMARY KEY, 
#     customer_id INTEGER, 
#     product TEXT,
#     category TEXT, 
#     quantity INTEGER, 
#     price REAL
# )
# ''')

customers = [
    (1, "Aanya", "Muscat"),
    (2, "Ishaan", "Muscat"),
    (3, "Prabhanjan", "Pune"),
    (4, "Vishal", "Pune"),
    (5, "Brinda", "Gujarat"),
    (6, "Saranya","Pune")
]

# cursor.executemany(
#     '''
#     INSERT INTO customers(customer_id, name, city)
#     VALUES(?,?,?)
#     ''', customers
# )

orders = [
    (101, 1, "Laptop", "Electronics", 1, 60000),
    (102, 1, "Mouse", "Electronics", 2, 800),
    (103, 2, "Keyboard", "Electronics", 1, 1500),
    (104, 3, "Chair", "Furniture", 2, 5000),
    (105, 3, "Desk", "Furniture", 1, 10000),
    (106, 4, "Laptop", "Electronics", 1, 60000),
    (107, 5, "Chair", "Furniture", 1, 5000)
]

# cursor.executemany("""
# INSERT INTO orders
# (order_id, customer_id, product, category, quantity, price)
# VALUES (?, ?, ?, ?, ?, ?)
# """, orders)

cursor.execute("""
    SELECT name, city
    FROM customers
    WHERE city = 'Pune'
""")


for row in cursor.fetchall():
    print(row)

cursor.execute("""
    SELECT * 
    FROM orders
    WHERE price > 10000
""")

for row in cursor.fetchall():
    print(row)


cursor.execute("""
    SELECT * 
    FROM orders
    WHERE price > 1000 
    AND 
    category = 'Electronics'
""")

for row in cursor.fetchall():
    print(row)
    
connection.commit()
connection.close()