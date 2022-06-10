class Student():
    
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender

    def getInformation(self):
        print("Hello")
    
    def greet(self,xyz):
        print("Hello " + xyz +"!")

student1 = Student(21, "Biplav", "Male")

print(type(student1))
print(student1.age)

student1.getInformation()
student1.greet("Yogesh")