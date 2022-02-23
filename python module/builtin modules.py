'''
   these modules are already available in python
'''

#let us take example of a module that generates random numbers

import random  #this module generates random numbers
import platform #this can detect the platform on whcih python is running
x=random.random()
print(x)   #it will generate a number 0<x<1 where x will be a float

#let us try to generate a random interger
y=random.randint(1,9999)  #it will generate a random number between the range 1 and 9999
print(y)

j=platform.system()   #it will fetch the value of operating system on which python is running
print(j)