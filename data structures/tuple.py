'''
      tuple:- a tuple is a list that cannot be changed
           it can be created using a parenthesis and with the help of a constructor
           elements in a tuple can be accessed with the help of their index
'''
#accessing elements
name=("name","sirname")
print(name)

for elements in name:    #elements can be accessed with the help of loop also
    print(elements)

print(name[0])   #to access a tuple with the help of index


#creating a tuple with the help of a tuple constructor
animals=tuple(("lion","dog","tiger","fox","bear"))
print(animals)

for animal in animals:
    print(animal)

print(len(animals))
#animals.add("dog") this will show error

#animals[0]=("cheetah") we cannot reassign elements in a tuple
#print(animals)

del animals #this will delete the tuple and next line will not be printed
print(animals)