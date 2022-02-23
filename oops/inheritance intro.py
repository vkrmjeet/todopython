'''
    it is a process that allows us to reuse methods and attributes from the super or parent class.
    the parent class is also known as super or base class.
    the child class is also known as derived class.
'''

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)


fn=input("please enter you firstname : ")
ln=input("please enter your lastname : ")
fnm=fn.upper()  #this will convert the first name into uppercase
a = Person(fnm,ln)
a.printname()