class Student:
    # non parameterized constructor
    def __init__(self):
        print("This is non parametrized constructor")
    def show(self):
        print("Hello")
student = Student()

'''class Student:
   # Constructor - parameterized
    def _init__(self, name):
        print("This is parametrized constructor")
        self.name = name
    def show(self):
        print("Hello",self.name)
student = Student("World")
student.show()'''