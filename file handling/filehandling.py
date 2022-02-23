'''
     syntax to open a file
         f = open("filename.extension") , the open function is used to open the file and it sets the file to the variable
         fn = open("filename.extension","accessmode") , if access mode is not defined then default access mode is set
              r or readonly is the default accessmode
'''

f = open("quotes.txt")
print(f.readable()) #this function will return the specification of file
#you cannot read the file directly from this function it will return the specification of file

# to read the file we have to use function
print(f.read())  # this will read the file and print it.

#you should close the file after using it for any task
f.close()

print(f.readable()) # this will return false as the file has already been closed.

