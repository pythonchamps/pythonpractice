class Student:
    def __init__(self,marks=10,cls='BE',name='StudentName'):
        self.marks = marks
        self.cls = cls
        self.name = name

    def __str__(self):
        return "Marks: {} and Class:{} and Name: {}".format(self.marks,self.cls,self.name)



std = Student(68,'mtech','Meghraj')
std1 = Student(80,'BTech','Prachi')
print(std)
print(std1)

