#Class Student Definition
class Student:

    def __init__(self,name='Ajay',roll='1',age='20'):
        self.name = name
        self.roll = roll
        self.age = age
        print("Parent Class Constructor")

    def getName(self):
        return self.name

    def getRoll(self):
        return self.roll

    def getAge(self):
        return self.age

    def __str__(self):
        return "Super class string"

class PhdStudent(Student):
    def __init__(self,name,roll,age, salary):
        super().__init__(name,roll,age)
        print("Child Class Constructor")
        self.salary = salary

    def getSalary(self):
        return self.salary

    def print_detail(self):
        print(self.__str__())
        print(super().__str__())

    def __str__(self):
        return "Sub Class String"

class College:
    def __init__(self):
        self.python_students = []
        self.java_students = []

    def admit_student(self,course,student):
        if(course == "Python"):
            self.python_students.append(student)
        elif(course == "Java"):
            self.java_students.append(student)

    def print_students(self,course):
        if(course == "Python"):
            for x in self.python_students:
                print(x.getName() + " " + str(x.getRoll()))
        else:
            for x in self.java_students:
                print(x.getName() + " " + str(x.getRoll()))


#st1 = Student("Meghraj",1,10)
#st2 = Student("Nilesh",2,11)
#st3 = Student("Brijmohan",3,14)

phs  = PhdStudent("Shivani",15,15,8000)

phs.print_detail()








