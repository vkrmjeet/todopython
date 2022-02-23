'''
    range : it is a built in function in python
            it is used to generate integers in between the range
            it starts with 0 by default if only one integer is used
            if two integers are given then it iterates through that range

            range(x,y)
            x is included in the range but y is not it stops at y-1
'''

for x in range(8):   #in this 8 is not included it will print only till 7
    print(x)

for x in range(1,9):
    print(x)

for x in range(2,20,4): #it will increment 4 after every iteration
    print(x)