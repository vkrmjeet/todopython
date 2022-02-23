'''
    class :- created with a keyword class followed by a name .
           a class can contain variables (attributes) and functions (methods)
           classes can be used to model a lot of things in the real world .
    self parameter is a reference to the current instance of the class. it is the first parameter of any method
    function in a class . it is used to access variables and methods belonging to the class. also used to add attributes
    to a method.
'''


class Instructors:
    a = 3
    company_name = "avis"

    def __init__(self, course):  # it is used to set an initial value to the variables ,
        # it is automatically called when a new object is created from the class
        self.course = course

    def printinfo(self):
        print("my company name is", Instructors.company_name)


# instantiate the above class : it means creating a object from a class
b = Instructors("python for beginners")
b.printinfo()

#accessing attribute :- it will access the course att
print(b.course)
