'''
     file pointer is the location of pointer in the file where we can perform any operation
     it determines the location where an operation will start
     tell() this method can be used to check the position of file pointer at any point of time
     seek() this method can be used to set the file pointer to any position
'''

f = open("quotes.txt")
print(f.tell())

print(f.readline(15))

print(f.tell())  # this will return 15 as we have already read 15 character from the file

f.seek(0) #this will set the file pointer position to 0

print(f.tell())

print(f.readlines())  #this will read the file from beginning as we have set our file pointer to zero.

f.close()