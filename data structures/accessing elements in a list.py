'''
          List can be accessed with the help of index
          the index of a list starts from 0
'''

animals= ["bear","panda","tiger","lion","jaguar"]

print(animals[1])   # only panda will be printed in this case
print(animals[2])   #tiger will be printed in this case


'''
we can also access elements from the opposite side of list by using negative index
'''

print(animals[-1])  # tiger will be printed in this case as the opposite index starts from negative 1 rather than
                    #zero


print(animals[1:])  #in this case the index will start from 1 and will compeletely ignore the element at the position zero



print(animals[1:3])  # it will print elements from the range 1 to 3


animals[0] = "dog"   # this will replace the element at position zero

print(animals)