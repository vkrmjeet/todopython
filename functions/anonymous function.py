'''
      they are also called lambda function
      they are defined by using the lambda keyword
      it can take several arguments but can have only one expression
'''

a = lambda b: b+4
print(a(4))  #the output will be 8 , the value passed to a is for the parameter b

c= lambda d,e: d+e
print(c(2,3))    #this will return the output i.e the sum of d and e

#they can be used when a function is required for a short period inside the other function

def ghost(n):
    return lambda f:f*n

double2 = ghost(4)
print(double2(3))