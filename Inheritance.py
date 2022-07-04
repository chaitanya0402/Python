'''class Animal:
    def speak(self):
        print("Animal Speaking")
#child class 
class Dog(Animal):
    def bark(self):
        print("dog barking")
d = Dog()
d.bark()
d.speak()'''


class sample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class sample1(sample):
    def __init__(self, marks, rollno):
        self.marks = marks
        self.rollno = rollno

    def show(self):
        print(self.marks, self.rollno)


s = sample1(55, 24)
s.display()
s.show()
