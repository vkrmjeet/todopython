'''
    let us try to implement basic exception handling
'''


x=20 #remove this line to cause an exception
try:
    print(x)
except:
    print("variable is not defined")
else:
    print("program is all good")
finally:
    print("program is fully executed")
