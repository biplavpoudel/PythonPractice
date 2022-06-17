from typing import ParamSpecArgs
from model.student import Student
from service.studentService import StudentService
import hashlib
import getpass

studentService = StudentService()


def add():        
    firstName = input("Enter firstName: ")
    lastName = input("Enter lastName: ")
    gender = input("Enter gender: ")
    age = input("Enter age: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    student = Student(firstName, lastName, gender, age, username, password)
    message = studentService.save(student)
    print(message)
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print(password)
    

def delete():
    ParamSpecArgs

def update():
    id = input("Enter student id to update: ")
    firstName = input("Enter updated firstName: ")
    lastName = input("Enter updated lastName: ")
    gender = input("Enter updated  gender: ")
    age = input("Enter updated age: ")
    username = input("Enter updated username: ")
    password = getpass.getpass("Enter updated password: ")

    
    student = Student(firstName, lastName, gender, age, username, password)
    student.id = id
    message = studentService.update(student)
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print(password)
    

def search():
    while(True):

        print("""\t\t 1.Search by firstname  \n
                 2.Search by lastname \n
                 3.Search by gender \n
                 4.Search by age  \n""")
        
        choice = input("Enter a choice: ")

        if choice == '1':
                pass
        elif choice == '2':
                pass
        elif choice == '3':
                pass
        elif choice == '4':
                pass
        else:
                print("Invalid choice. \n")
    
def list():
    students = studentService.list()
    for student in students:
        print(student.id, student.firstName, student.lastName, student.gender, student.age, student.username)

def initialize():
    while (True):
        print("""\n1.Add
                \n2.List
                \n3.Delete
                \n4.Update
                \n5.Search""")
        choice = input("\nEnter a choice: ")

        if choice == '1':
            add()
        elif choice == '2':
            list()
        elif choice == '3':
            delete()
        elif choice == '4':
            update()
        elif choice == '5':
            search()
        else:
            print("Invalid choice. \n")



if __name__ == '__main__':
    initialize()