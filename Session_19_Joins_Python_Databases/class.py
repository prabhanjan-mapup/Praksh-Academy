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

# customers = [
#     (1, "Aanya", "Muscat"),
#     (2, "Ishaan", "Muscat"),
#     (3, "Prabhanjan", "Pune"),
#     (4, "Vishal", "Pune"),
#     (5, "Brinda", "Gujarat"),
#     (6, "Saranya","Pune")
# ]

# cursor.executemany(
#     '''
#     INSERT OR IGNORE INTO customers(customer_id, name, city)
#     VALUES(?,?,?)
#     ''', customers
# )

# orders = [
#     (101, 1, "Laptop", "Electronics", 1, 60000),
#     (102, 1, "Mouse", "Electronics", 2, 800),
#     (103, 2, "Keyboard", "Electronics", 1, 1500),
#     (104, 3, "Chair", "Furniture", 2, 5000),
#     (105, 3, "Desk", "Furniture", 1, 10000),
#     (106, 4, "Laptop", "Electronics", 1, 60000),
#     (107, 5, "Chair", "Furniture", 1, 5000)
# ]

# cursor.executemany("""
# INSERT OR IGNORE INTO orders
# (order_id, customer_id, product, category, quantity, price)
# VALUES (?, ?, ?, ?, ?, ?)
# """, orders)

# cursor.execute("""
#     SELECT name, city
#     FROM customers
#     WHERE city = 'Pune'
# """)


# for row in cursor.fetchall():
#     print(row)

# cursor.execute("""
#     SELECT * 
#     FROM orders
#     WHERE price > 10000
# """)

# for row in cursor.fetchall():
#     print(row)


# cursor.execute("""
#     SELECT * 
#     FROM orders
#     WHERE price > 1000 
#     AND 
#     category = 'Electronics'
# """)

# for row in cursor.fetchall():
#     print(row)


# customers = [
#     (1, "Aanya", "Pune"),
#     (2, "Rahul", "Mumbai"),
#     (3, "Priya", "Pune"),
#     (4, "Arjun", "Delhi"),
#     (5, "Neha", "Mumbai"),
#     (6, "Riya", "Nashik")
# ]

# cursor.executemany("""
#     INSERT  INTO customers(customer_id, name, city)
#     VALUES(?,?,?)
# """,customers)




'''
Alter - edit the schema of the table 
syntax :
ALTER TABLE <table_name>
ADD COLUMN <column_name> <datatype>


'''
# cursor.execute("""
#     ALTER TABLE customers
#     ADD COLUMN email TEXT
# """)

# cursor.execute("""
#     ALTER TABLE customers
#     ADD COLUMN phone TEXT
# """)

# cursor.execute("""
#     ALTER TABLE customers
#     ADD COLUMN registration_date TEXT
# """)

# cursor.execute("""
#     ALTER TABLE orders
#     ADD COLUMN order_date TEXT
# """)

# cursor.execute("""
#     ALTER TABLE orders
#     ADD COLUMN status TEXT
# """)

'''
UPDATE - we are updating the existing records data. 
Syntax: 
UPDATE <table_name>
SET
    <column_name> = value,
    <column_name> = value,
    .
    .
    .
WHERE <column_name(primary_keys)> = value

'''


# cursor.execute("""
#     SELECT * 
#     FROM customers
# """)

# for row in cursor.fetchall():
#     print(row)

# cursor.execute("""
#     UPDATE customers
#     SET
#         email = 'aanyagoyal@gmail.com',
#         phone = '123456789',
#         registration_date = '2026-07-22'
#     WHERE customer_id = 1
# """)

# cursor.execute("""
#     UPDATE customers
#     SET
#         email = 'prabhanjanbhosale@gmail.com',
#         phone = '1234567891',
#         registration_date = '2026-07-22'
#     WHERE customer_id = 3
# """)
# cursor.execute("""
#     SELECT * 
#     FROM customers
# """)

# for row in cursor.fetchall():
#     print(row)


# more_customers = [
#     (7, "Karan", "Pune", "karan@gmail.com", "9876500007", "2026-04-01"),
#     (8, "Sneha", "Bengaluru", "sneha@gmail.com", "9876500008", "2026-04-08"),
#     (9, "Amit", "Delhi", "amit@gmail.com", "9876500009", "2026-04-15"),
#     (10, "Pooja", "Mumbai", "pooja@gmail.com", "9876500010", "2026-04-20"),
#     (11, "Vikram", "Pune", "vikram@gmail.com", "9876500011", "2026-04-25"),
#     (12, "Isha", "Nashik", "isha@gmail.com", "9876500012", "2026-05-02"),
#     (13, "Rohan", "Bengaluru", "rohan@gmail.com", "9876500013", "2026-05-10"),
#     (14, "Meera", "Delhi", "meera@gmail.com", "9876500014", "2026-05-15"),
#     (15, "Aditya", "Mumbai", "aditya@gmail.com", "9876500015", "2026-05-22")
# ]

# cursor.executemany(
#     '''
#     INSERT OR IGNORE INTO customers(customer_id, name, city, email, phone, registration_date)
#     VALUES(?,?,?,?,?,?)
#     ''', more_customers
# )

# more_orders = [
#     (108, 7, "Monitor", "Electronics", 2, 15000, "2026-04-05", "Completed"),
#     (109, 8, "Desk", "Furniture", 1, 10000, "2026-04-10", "Completed"),
#     (110, 9, "Keyboard", "Electronics", 2, 1500, "2026-04-16", "Pending"),
#     (111, 10, "Laptop", "Electronics", 1, 60000, "2026-04-21", "Completed"),
#     (112, 11, "Chair", "Furniture", 4, 5000, "2026-04-27", "Completed"),
#     (113, 12, "Mouse", "Electronics", 3, 800, "2026-05-03", "Cancelled"),
#     (114, 13, "Monitor", "Electronics", 1, 15000, "2026-05-11", "Completed"),
#     (115, 14, "Desk", "Furniture", 2, 10000, "2026-05-16", "Pending"),
#     (116, 15, "Laptop", "Electronics", 2, 60000, "2026-05-23", "Completed"),
#     (117, 2, "Mouse", "Electronics", 1, 800, "2026-05-25", "Completed"),
#     (118, 5, "Desk", "Furniture", 1, 10000, "2026-05-26", "Completed"),
#     (119, 6, "Keyboard", "Electronics", 1, 1500, "2026-05-27", "Pending"),
#     (120, 8, "Chair", "Furniture", 2, 5000, "2026-05-28", "Completed"),
#     (121, 1, "Monitor", "Electronics", 1, 15000, "2026-06-01", "Completed"),
#     (122, 3, "Mouse", "Electronics", 2, 800, "2026-06-02", "Completed"),
#     (123, 7, "Chair", "Furniture", 1, 5000, "2026-06-03", "Pending"),
#     (124, 10, "Keyboard", "Electronics", 3, 1500, "2026-06-05", "Completed"),
#     (125, 12, "Desk", "Furniture", 1, 10000, "2026-06-07", "Completed"),
#     (126, 14, "Laptop", "Electronics", 1, 60000, "2026-06-10", "Completed"),
#     (127, 15, "Mouse", "Electronics", 5, 800, "2026-06-12", "Pending")
# ]

# cursor.executemany("""
# INSERT OR IGNORE INTO orders
# (order_id, customer_id, product, category, quantity, price, order_date, status)
# VALUES (?, ?, ?, ?, ?, ?, ?, ?)
# """, more_orders)

# cursor.execute("""
#     SELECT * 
#     FROM orders
# """)

# for row in cursor.fetchall():
#     print(row)
"""Alias we use AS keyword """
# cursor.execute("""
#     SELECT 
#         name AS customer_name, 
#         city AS customer_city
#     FROM customers
# """)

# cursor.execute("""
# SELECT * 
# FROM customers 
# WHERE city = 'Pune' 
# OR city = 'Mumbai'
# OR city = 'Delhi'
# """)

# cursor.execute("""
# SELECT * 
# FROM customers
# WHERE city IN ('Pune','Mumbai','Delhi') 
# """)

# cursor.execute("""
# SELECT * 
# FROM orders
# WHERE price>=5000 AND price<=20000
# """)
# cursor.execute("""
# SELECT * 
# FROM orders
# WHERE price BETWEEN 5000 AND 20000
# """)

'''
LIKE - This operator is used to filter out the rows on the basis of patterns
1. starts with - <characters>%
2. end with - %<characters>

'''
# cursor.execute("""
# SELECT * 
# FROM customers
# WHERE name LIKE '%an%'
# """)

# cursor.execute("""
# SELECT * 
# FROM customers
# WHERE email is NULL
# """)
# cursor.execute("""
# SELECT * 
# FROM customers
# WHERE email is NOT NULL
# """)

# cursor.execute("""
# SELECT COUNT(*) FROM orders
# WHERE status = 'Pending'
# """)

cursor.execute("""
SELECT 
    category,product,  SUM(quantity*price) AS total_sales
FROM orders
GROUP BY category, product
HAVING SUM(quantity*price) > 5000
""")

# cursor.execute("""
# SELECT
#     category,
#     product,
#     COUNT(*) as order_count
# FROM orders
# WHERE status = 'Pending'
# GROUP BY category, product
# """)

# print(cursor.fetchone())
for row in cursor.fetchall():
    print(row)
connection.commit()
connection.close()


#Left with Joins. - upcoming doubtsession