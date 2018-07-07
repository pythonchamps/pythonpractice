class Student:
    def __init__(self,name='Test'):
        self.name = name
        print("Student Constructor Called")

    def getName(self):
        return self.name

class PhdStudent(Student):
    def __init__(self,name,salary):
        self.salary = salary
        self.name = name
        print("PhdStudent Constructor called")
        super().__init__(name)

    def getName(self):
        print("Child Class")
        return self.name


pst = PhdStudent('student',1000)
print(pst.getName())



