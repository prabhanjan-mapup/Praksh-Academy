'''
query = "sample query"
cursor.execute(query)
result = cursor.fetchall()[fetchone(), fetchmany(size)]

'''
import sqlite3

connection = sqlite3.connect('restaurant.db')
cursor = connection.cursor()
'''
Create a table - 
syntax : 
CREATE TABLE IF NOT EXISTS table_name(
column1 dataype Primary Key,
column2 datatype , 
column3 dataype
)

'''
cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS hotel(
        FID INTEGER PRIMARY KEY NOT NULL, 
        FNAME TEXT NOT NULL, 
        COST INTEGER  NOT NULL,
        WEIGHT INTEGER
        )
    '''
)

'''
syntax : insert data

INSERT INTO table_name VALUES(value1, value2, value3)
'''

# cursor.execute("INSERT INTO hotel (FID, FNAME, COST, WEIGHT) VALUES(1, 'Cakes', 800, 1000)")
# cursor.execute("INSERT INTO hotel (FID, FNAME, COST, WEIGHT) VALUES(2, 'Biscuit', 40, 100)")
# cursor.execute("INSERT INTO hotel (FID, FNAME, COST, WEIGHT) VALUES(3, 'Doughnuts', 60, 20)")
# cursor.execute("INSERT INTO hotel (FID, FNAME, COST, WEIGHT) VALUES(4, 'Cupcakes', 20, 100)")
# cursor.execute("INSERT INTO hotel (FID, FNAME, COST, WEIGHT) VALUES(5, 'Pastry', 50, 150)")



'''
Select statement
1. Select * from table_name - here you will retreive all the columns from the table
2. Select col_1, col_2 from table_name
'''
cursor.execute("SELECT * FROM hotel")
rows = cursor.fetchall()

for row in rows:
    print(row)


connection.commit()
connection.close()