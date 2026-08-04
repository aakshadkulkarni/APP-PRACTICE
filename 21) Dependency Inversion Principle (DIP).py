class Student:
    def message(self):
        print("Name: Aakshad")
        print("College: MIT ADT")

class Display:
    def __init__(self, obj):
        self.obj = obj

    def show(self):
        self.obj.message()

s = Student()
d = Display(s)
d.show()
