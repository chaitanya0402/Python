class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name, self.age)
emp1=employee("Chaitanya",22)
emp2=employee("Sid",33)
emp1.display()
emp2.display()

