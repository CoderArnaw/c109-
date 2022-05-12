class Student(object):
    def __init__(self,name,grade,age):
        self.name=name
        self.grade=grade
        self.age=age
    def getGrade(self,course,grade):
        self.grade[course]=grade
    def getGrade(self,course):
        return self.grades[course]        

arnav=Student("arnav",8,14)
print(arnav.grade)

class Car(object):

    def __init__(self,color,name,speed,company):
        self.color=color
        self.name=name
        self.speed=speed
        self.company=company
    def getStart(self):
        print("car has started") 

    def getStop(self):
        print("car has stopped") 

Lamborghini=Car('red',"urus",250,"lamborghini")
print(Lamborghini.speed)
print(Lamborghini.getStart())
