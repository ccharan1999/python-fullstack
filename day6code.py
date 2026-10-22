class Student :
    def __init__ (self, name, course,marks, age, sex) :

        self.name = name
        self.course = course
        self.marks = marks
        self.age = age
        self.sex = sex
        self.marks=[]

    def addmarks(self,marks):
         self.marks.append(marks)


    def findavg(self):
        return sum(self.marks) / len(self.marks)

student1 = Student ("charan","math",50,10,"male")
student1.addmarks(77)
student1.addmarks(88)
print(student1.marks)

print(student1.findavg())



