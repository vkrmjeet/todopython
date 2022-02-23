'''
    nesting functions :- a nested function (or nested procedure or subroutine) is
                         a function which is defined within another function, the enclosing function.
'''

def func(a):
    def func2(a):
        return a+1  
    result = func2(a)
    return result
print(func(3))


'''
    nesting function accessing variable scopes
'''
def displaymessage(message):
    "hello"
    def message_sender():
        "nested function"
        print(message)
    message_sender()

displaymessage("hello bro")