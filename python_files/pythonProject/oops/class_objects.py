#OOPS
#object oreiented programming language
#classes & objects
class Student:
    def __init__(self,name,age,grade): #innit is called constructor
        self.name = name #instance variables
        self.age = age
        self.grade = grade

    def get_details(self):
        print(f"name:{self.name}, Age:{self.age}, grade: {self.grade}")

    def update_grade(self,new_grade):
        self.grade = new_grade

student1 = Student("jhon",23,'A')#constructor method is called every time an object is created
student1.get_details()
student1.update_grade("A+")
student1.get_details()

student2 = Student("jane",24,'B') #constructor method is called automatically
student2.get_details()