'''
     set :- it is a type of data structure in python
            A set is a collection of values
            values in a set are not ordered
            values in a set are not indexed
            values can be added but cannot be changed
'''

#creating a set
fruits={"grapes","apples","berries"}
print(fruits) #printing values of a set

#using loop to print the values of a set
for x in fruits:
    print(x)

#creating a set with the help of a constructor
animals=set(("lion","bear","tiger"))
print(animals)

for y in animals:
    print(y)

print(len(animals)) #this will return the number of values from the set 