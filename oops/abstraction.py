'''
    abstraction :- abstraction is used to hide the internal details and show only the functionality that is required
    abstract classes :- these classes contain one or more abstract methods
                        abstract classes cannot be instantiated
                        they require subclasses to implement the functionality
    abstract method :- these methods are declared but doesn't contain implementation where the are declared
'''

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):   #this class is abstract we cannot instantiate it
        pass

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*self.side

#myshape = Shape()  this should be commented out as we cannot create object of abstract class
#mysq = Square()  this will also show error if the implementation of abstract class is not provided

mysqu = Square(5)   #this will run without error as the abstract methods are overloaded in the child class
print(mysqu.area())
print(mysqu.perimeter())