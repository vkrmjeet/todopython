f = open("quotes.txt")

#print(f.read(15))  #this will return the character at the first 15 characters of the file

#print(f.readlines(0))  #this will return the lines that have not been read before, and return the remaining unread file as a list

for quote in f:
    print(quote)

f.close()