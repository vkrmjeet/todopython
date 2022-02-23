class Shape(ABC):
    def area(self):
        pass
    def perimeter(self):   #this class is not abstract yet so it can be instantiated
        pass

class Square(Shape):
    def __init__(self,side):
        self.side = side

myshape = Shape()
