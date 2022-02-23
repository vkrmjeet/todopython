'''
     Python dictionary :- A dictionary is a collection of key value pairs
                         values must have unique keys
                         the values can be changed
                         mixed datatype can be stored
'''

#there are different ways a dictionary can be created

mycar={"brand":"range rover sports"
        , "model":"hse"
        ,  "year":2017 }
print(mycar["brand"])   #this will print the brand of the car when we specify the key it will print the value for that key


#a dictionary can also be created with the help of dictionary creator function
mygreens=dict(fruit="apple",vegetable="sweet potato",)
print(mygreens['vegetable'])