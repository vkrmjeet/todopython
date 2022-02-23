'''
    DRY :- this principle is used by programmers it means dont repeat urself, functions helps us to attain that
         because ther are reusable
    functions :- functions are pieces of code that does something
                 they are reusable
                 they execute or run when they are called
                 they can have parameters and values
                 they can return data as well
                 there are builtin functions for ex print
                 there can also be user defined functions that can be created by users
    :parameter :- A parameter is a variable defined inside a function's parenthesis
    :argument :-  an argument is the actual value you pass to the function when it is called
'''

def printhello():
    print("hello world")
printhello()
printhello()

x=input("enter a number : ")
y=input("enter a number : ")

def sum(x,y):    #we have created a function here that takes two parameters and return the sum of those parameters
    print(int(x)+int(y))
sum(x,y)       #here we have called the functions and passed two values to it
sum(2,3)       #here we can also pass the values directly