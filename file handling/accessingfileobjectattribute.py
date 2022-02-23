f = open("quotes.txt")

print(f.name)  # this will print the name of the file
print(f.mode)  #this will print the accessmode of the file , in this case it will give r rwhich is the default mode
print(f.closed) #this will return a boolean value checking the status of file , in this case it will return false as file is still open

f.closed

print(f.closed) #this will return true