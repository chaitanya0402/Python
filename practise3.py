'''class A:
    def test1(self):
        print("Parent A")
class B:
    def test2(self):
        print("Parent B")
class C(A,B):
    def test3(self):
        print("Child class")
c1=C()
c1.test1()
c1.test2()
#c1.test3()
print(issubclass(C,B))     #gives boolean values depending upon paramters
print(issubclass(A,C))
print(isinstance(c1,B)) '''   #checks whether the object belongs to particular class

#method overriding
class D:
    def __init__(self,name):
       self.name=name
    def display(self):
        print("Bike")
class E(D):
    def __init__(self,age):
        super().__init__("Hii")
    def display(self):
        print("Car")
class F(E):
    def __init__(self,id):
        super().__init__(22)
        def display(self):
            print("Bicycle")
obj=E(23)
obj1=F(20)
obj.display()
obj1.display()



