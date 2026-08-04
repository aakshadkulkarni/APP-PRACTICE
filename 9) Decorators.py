def welcome(fun):
    def msg():
        print("Welcome")
        fun()
    return msg

@welcome
def student():
    print("Aakshad - MIT ADT")

student()
