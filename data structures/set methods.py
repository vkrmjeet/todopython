'''
    add()        :- add an element to the set
    update()     :- add multiple element to the set
    clear()      :- removes all element from the set
    discard()    :- removes a specified element or item from a set
    remove()     :- removes a specified item from the set
    del()        :- delete the set
    remove and discard method do the same thing
'''

fruits={"apple","banana","peach"}
animmals={"dog","lion","tiger"}

fruits.add("oranges")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.discard("oranges")
print(fruits)

fruits.update(["oranges","banana"])
print(fruits)

fruits.clear()
print(fruits)  #this will print set() depicting that the set is empty

animmals.clear()
print(animmals)