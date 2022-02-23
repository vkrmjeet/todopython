class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)


a=Person("abc","xyz")
a.printname()

class Lawyers(Person): #this will inherit the person class and any class that is mentioned inside the class_name(Parent class)
    pass #this means this class does not have any method

happy_lawyers = Lawyers("julie","julie")
happy_lawyers.printname()  #with this we can access the function called printname that belongs to the parent class
