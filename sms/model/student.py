class Student():
    
    def __init__(self, firstName, lastName, gender, age, username=None, password=None, id=None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.age = age if age else None
        self.gender = gender if gender else ""
        self.username = username if username else ""
        self.password = password if password else "" 