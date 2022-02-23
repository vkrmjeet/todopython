'''
    nested for loops :- a nested loop is a loop inside another loop

'''

a = ["apple", "banana"]
b = ["orange", "mango"]

for x in a:
    for y in b:
        print(x,y)

m1 = [1,2,3]
m2 = [4,5,6]

for c in m1:
    for d in m2:
        print(c*d)