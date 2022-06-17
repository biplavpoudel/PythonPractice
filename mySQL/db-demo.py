import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Luxarcadian@@007"
)

print(db)

dbQuery = "CREATE DATABASE IF NOT EXISTS ems"

cursor = db.cursor()
cursor.execute(dbQuery)

cursor.execute("USE ems")

empTable = """
    CREATE TABLE IF NOT EXISTS employee(
        id INT PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(20) NOT NULL,
        age INT
    )"""

cursor.execute(empTable)

# insert = """
#     insert into employee values
#     (1, 'Yogesh', 'Bhandari', 21),
#     (2, 'Sharad', 'Baucha', 22),
#     (3, 'Shyam', 'Rimal', 26);
# """

# cursor.execute(insert)
# db.commit()

# update ="""
#     update employee
#     set first_name = 'Kusume'
#     where id = 3;
# """

# cursor.execute(update)
# db.commit()

delete ="""
    DELETE from employee
    WHERE id = 5;
"""
cursor.execute(delete)
db.commit()