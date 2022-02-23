'''
    list methods
       index():- this method is used to return the index position of a specified item
'''

fruits=["mango","banana","apple","peach"]
vegetable=["tomato","potato","onion","spinach"]


print(fruits.index("banana"))    # this will return the index of banana from the list fruits


#insert method is used to add a new item in the list
fruits.insert(0,"berries")
print(fruits)
print(fruits.index("banana"))



#pop method is used to remove the last item from the list when nothing is specified but if index is
#specified then it will remove the item at that position
fruits.pop()    #this will remove the last item from the list
print(fruits)
fruits.pop(1)   #this will remove the value at index 1
print(fruits)
fruits.remove("banana") #this will remove banana from the list
print(fruits)

#to delete a list fully we can do so by using the keyword del
del vegetable
#print(vegetable) this will show error


fruits.append("banana")