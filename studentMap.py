class Student:
    def __init__(self,roll,name,marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.marks = list(map(int,self.marks))
        self.average = sum(self.marks)/len(self.marks)

    def __del__(self):
        pass

    def get_marks(self):
        return self.marks

    def get_name(self):
        return self.name

    def get_roll(self):
        return self.roll

    def get_average(self):
        return self.average

    def get_data(self):
        return [self.roll,self.name,self.marks,self.average]

    def __str__(self):
        return "Name:{} and Average:{}".format(self.get_name(),self.get_average())

class StudentMap:
    def __init__(self,filename):
        self.file = open(filename,"r")
        self.student_list = []
        self.map_file()

    def map_file(self):
        for line in self.file:
            line = line.strip()
            lst = line.split(",")
            self.student_list.append(Student(lst[0],lst[1],lst[2:]))

    def get_students(self):
        return self.student_list

    def get_first_division(self):
        return [x for x in students if x.get_average()>=60]

    def get_second_division(self):
        return [x for x in students if x.get_average()>=50 and x.get_average()<60 ]

    def get_third_division(self):
        return [x for x in students if x.get_average()<50]

    def get_in_range(self,min=0,max=100):
        return [x for x in students if x.get_average()>=min and x.get_average()<=max ]




if(__name__ == "__main__"):
    stud_map = StudentMap("practice.csv")

    #stud_map.map_file()

    students = stud_map.get_students()

    students_first_division = stud_map.get_first_division()
    students_second_division = stud_map.get_second_division()
    students_third_division = stud_map.get_third_division()
    print(len(students_first_division))
    print(len(students_second_division))
    print(len(students_third_division))
    print(students_first_division)

    print(list(map(str,students_first_division)))

