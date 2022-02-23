'''
find() :- this method is used to find out first index occurence of a string of characters
'''
a="hello world."
print(a.find("world")) #this will return 6 value the position of index for the word world


'''
count() :- this method is used to count the occurence of a string or character
'''
print(a.find("l")) #this will return 2 value


'''
split() :- this method is used to split a string into a python list
'''
print(a.split()) #this will split the string in a array of words that the string contains


'''
\n :- this character is used to start a new line
'''
print("hello \nworld")




''''
+ :- concatenation operator
'''
print(a + " Today is a good day.")





'''
replace() :-  this method can replace string or characters 
takes two parameters one to replace and other to replace with
'''
print(a.replace("world.","bro")) #this will print Hello bro