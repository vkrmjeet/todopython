'''
        A list is a collection of data which can be of mixed data type
        The items in the list are ordered by their index and their position can be changed
        List are created by using square brackets []
        list can be blank
        the items in a list can be accessed with the help of their index
        each item in the list has to be separated by a comma
        it is very useful as it allows to store multiple values in a container
'''

# creating a python list
animals=["bear", "lion", "tiger","panda"]

#you can also create list using a constructor which is a function used to create objects
animal=list(("bear","lion","tiger"))

#print(animal)
#print(animals)

for x in animals:
    print(x)
print(animals)
