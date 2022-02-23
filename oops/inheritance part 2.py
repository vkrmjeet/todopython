'''
    let us add init in the child class
    if we do not add init it inherits all the methods from the parent class
    if init is given to it , it overrides all the methods of the parent class
'''

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

a=Person("parent","class")
a.printname()

class Lawyers(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
        #self.firstname=fname
        #self.lastname=lname
    def print(self):
        print(self.firstname,self.lastname)

b=Lawyers("child","class")
b.printname()
b.print()