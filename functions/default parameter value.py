'''
     this is the value a function used when it is called without passing a value
     only parameters at the end of a parameter list can have a default value as values are assigned by the position
     default parameter can only be given to the last variable
'''
'''
def sum(a,b=7):    #if both the argument arent provided then it will show error when it is called without passing parameters
    return a+b

print(sum())
'''
def stu_names(name="boby"):
    print("hello "+name)

stu_names()          #even if the parameter is not passed in this function there is already a default parameter in the function
stu_names("bhalu")
stu_names("boi")