'''
     a decorator is a design pattern in python that allow a user to add a new functionality to existing objects like
     functions , methods and classes
     without affecting its structure
     the decorators are usually called before the definition of the object (function , class , method)
     we want to decorate.
     they can be represented by @ followed by the name of the object.
'''

#creating a decorator , it will convert a sentence to uppercase
def mydecoration(function):
    def wrapper():
        myfunc=function()
        convert_uppercase = myfunc.upper()
        return convert_uppercase
    return wrapper
@mydecoration
def say_hello():
    return "hello world!"
print(say_hello())

#decorate = mydecoration(say_hello) , this method can be used when we dont use @ before the function to be decorated
#print(decorate())