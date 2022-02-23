'''
      once created a module can be used in any python file
      it can be done by importing the file
         ex:- import module_name
      specific things can also be imprted from a module
         ex:- module_name import(what you need)
'''

#the module with name module will be imported in this program
import module   #directly importing the whole module
from module import fruits
module.say_hello("vikramjeet")

print(fruits["name"])   #this will print the name of the fruit