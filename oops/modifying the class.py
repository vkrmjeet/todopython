'''
      modifying the class :-
      add new Attributes
      modify existing attribute values
      delete attributes
'''

class Instructors:
    a = 3
    company_name = "avis"

    def __init__(self, course , duration):  # it is used to set an initial value to the variables ,
        # it is automatically called when a new object is created from the class
        self.course = course
        self.duration = duration

    def printinfo(self):
        print("my company name is", Instructors.company_name)


# instantiate the above class : it means creating a object from a class
b = Instructors("python for beginners" , 5)
b.printinfo()

#accessing attribute :- it will access the course attribute
print(b.course,"for duration ",b.duration)

#edit an attribute
b.duration=6
print(b.course,"for duration ",b.duration)

#delete an attribute
del b.duration

print(b.duration) #this will give an error because it was deleted on line 33