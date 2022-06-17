import mysql.connector

from model.student import Student

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Luxarcadian@@007",
  database = "ems"
)

create_student_table = """
CREATE TABLE IF NOT EXISTS student(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(15),
    age INT,
    username VARCHAR(50),
    password VARCHAR(50)
)
"""

dataBase.cursor().execute(create_student_table)

class StudentDao():

    def save(self, student):
        print(student.gender)
        query = f"""
                INSERT INTO student (first_name, last_name, gender, age, username, password) VALUE
                ('{student.firstName}','{student.lastName}','{student.gender}', '{student.age}','{student.username}', '{student.password}')
        """ 
        cursor = dataBase.cursor()
        cursor.execute(query)
        dataBase.commit()
    
    def list(self):
        students = []

        query = """
                SELECT * FROM student
        """ 
        cursor = dataBase.cursor()
        cursor.execute(query)
        resultSet = cursor.fetchall()

        for emp in resultSet:
            print(type(emp))
            print(emp)
            students.append(Student(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5]))
        
        return students

    def update(self, student):
        query = f"""
                    update student set first_name = '{student.firstName}', last_name = '{student.lastName}',
                    gender = '{student.gender}', age = '{student.age}', username = '{student.username}',
                    password = '{student.password}' where id = '{student.id}'
        """
        print(query)

        cursor = dataBase.cursor()
        cursor.execute(query)
        dataBase.commit()
