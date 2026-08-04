class Person:
    def info(self):
        print("Person")

class Student(Person):
    def info(self):
        print("Student: Aakshad")

p = Student()
p.info()
