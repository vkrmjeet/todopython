'''
variables that are defined inside a function have a local scope
variables that are defined outside the function have a global scope

global variables can be accessed anywhere in your python file
local variables can be accessed inside the function it belongs to
'''

#global keyword can be used inside a function definition to make the variable global

'''
x=10

def my_numbers(x):
    print(x)
    x=5  this will not change the value of x outside the function
    print("my favorite number : ", x)

my_numbers(x)
print(x)
'''

x=10

def my_numbers():     #we shouldn't pass the global variable here if we do it will show error as it is already global
    global x
    print(x)
    x=5
    print("my favorite number : ", x)

my_numbers()
print(x)