from dao.studentDao import StudentDao

class StudentService():

    studentDao = StudentDao()

    def save(self, student):
        try:
            self.validatestudent(student)
            self.studentDao.save(student)
            message = "Save Successful"
        except Exception as e:
            message = "Failed to Save record" + str(e.args)
    
        return message

    def validatestudent(self, student):
        if student.firstName is None or student.firstName == "":
            raise Exception("First Name is invalid")
        if student.lastName is None or student.lastName == "":
            raise Exception("Last Name is invalid")

    def list(self):
        return self.studentDao.list()

    def update(self,student):
        # return self.studentDao.update()
        try:
            self.validatestudent(student)
            self.studentDao.update(student)
            message = "Update Successful"
        except Exception as e:
            message = "Failed to update record" + str(e.args)
    
        return message
           
