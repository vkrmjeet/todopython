'''
len()  :- this method is used to find the total length of a string
'''
a="my name is bla"
print(len(a)) #this will return 14 value . it also includes spaces while calculating the total characters in a string


'''
index() :- this method is used to return the position of a string or character
'''
print(a.index("name")) #this will return value 3 as the index starts from 0 the name word start from the position 3


'''
capitalize() :- this method converts the first character of a word to uppercase
'''
print(a.capitalize())


'''
upper() :- this converts a string to upper case
'''
print(a.upper())


'''
lower() :- similar to upper method this converts the upper method to lowercase
'''
print(a.lower())



'''
isupper() :- this checks if a string is in uppercase or not
islower() :- this checks if a string is in lowercase or not
'''
print(a.islower())
print(a.isupper())