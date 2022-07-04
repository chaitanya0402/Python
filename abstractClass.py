from abc import ABC,abstractmethod
class AbstractionAnimal(ABC):
    @abstractmethod
    def bark(self): pass


class Dog(AbstractionAnimal):
    def bark(self):
        print("Bow Bow")

print(Dog().bark())
