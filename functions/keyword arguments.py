'''
     allow you to specify what parameterrs to use from a list of parameters
     you do not need to worry about the order of arguments
     allows you to give values only to parameters you want provided the other parameters have default argument values
'''

def more_num(a,b=2,c=3):
    print("a is ",a," and b is ",b," while c is",c)


more_num(2)      #in this we can provide only one value and that value will be given to the variable that is unintialized
                #in the above functions that is a

more_num(5,b=5)    #this will intialize a is equal to 5 and b is equal to 5

more_num(c=6 , a=10)   #this will pass the following values


more_num(10,11)   #this will pass the following values in the order of parameters in the function i.e a=10 and b=11