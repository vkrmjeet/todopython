'''
using f string
f string :- it is a string literal prefixed with a letter f
            it contains expression which are inside curly braces which are replaced with actual values
            it is an expression which is evaluated at runtime and formatted at runtime
            they are not constant values they are only evaluated at runtime
            it doesnt matter if f is uppercase or lowercase
'''


name="appleboy"
age= 15

f"Hello,{name}. You are {age} years old ." #this will run in python console and return
                                           #'Hello,appleboy. You are 15 years old '

f"{7+7}"  #this will return '14' as python treats it as a string rather than an interger

f"{name.upper()} is {age} years old"   #this will return 'APPLEBOY is 15 years old' in console
