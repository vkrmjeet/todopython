'''
   List methods
   extend add two lists
   append add an element at the end of a list

'''

fruits=["mango","banana","apple","peach"]
vegetable=["tomato","potato","onion","spinach"]

fruits.extend(vegetable)
print(fruits)

vegetable.append("bean")
print(vegetable)


'''
     sort method is used to sort elements in a list in ascending or descending order
     
'''
vegetable.sort()     #this will print the list in ascending order
print(vegetable)

vegetable.sort(reverse=True)     #this will print the list in descending order
print(vegetable)



'''
    count method :- it counts the number of occurence of an item
'''

print(vegetable.count("potato"))    #this will give a count of 1
print(vegetable.count("banana"))    #this will give a count of 0 as banana doesn't exist in the vegetable table

vegetable.add("bla")
