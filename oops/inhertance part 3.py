'''
    adding attributes in the child class
'''

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

a=Person("parent","class")
#a.printname()

class Child(Person):
    def __init__(self,fname,lname,casetype):
        Person.__init__(self,fname,lname)
        self.casetype=casetype

    def printinfo(self):
        print("hello my name is",self.firstname,self.lastname,self.casetype)

b=Child("child","class","criminal")
b.printinfo()
b.printname()

print(b.casetype)

#when two classes have same method names the method of child class takes precedence