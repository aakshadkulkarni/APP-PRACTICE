class Student:
    def show(self):
        print("Student: Aakshad")

class Factory:
    def create(self):
        return Student()

f = Factory()
obj = f.create()
obj.show()
