class encap:
    def __init__(self):
        self.__a=5                   #private variable start with underscore
    def show(self):
        print(self.__a)
    def s(self,b):
        self.__a=b
e1=encap()
e1.show()
e1.__a=6
e1.show()
e1.s(20)
e1.show()
