class Student:
    def show(self):
        print("Student: Aakshad")

class Teacher(Student):
    def show(self):
        print("Teacher: ABC")

s = Student()
t = Teacher()

s.show()
t.show()
