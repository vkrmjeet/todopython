'''
     document strings
     allow you to display documentation when code executes
     they are accessed by using double underscore with attribute name
     they are defined by using three single quotes and some text in it.
'''

def addnum(d,e):
    '''adding these two numbers.
       the values that are passed to this function will be added
       the value must be integers'''
    print(d+e)

addnum(2,3)   # this will print the sum of the numbers that are passed as parameters in it

#to print the docstring
print(addnum.__doc__)   #this will print the documentation . help() and pydoc() functions can provide more information about doc strings