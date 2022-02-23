f = open("quotes.txt","a")  #the mode is a which means the file is going to be appended

f.write("\nbe happy in your life , nothing stays same forever")

#\n is used to append the file in a new line.
#be sure to use the right accessmode
#if we don't use append in this case then the file will be overwritten

#suppose if we use,  f = open("quotes.txt","w") then the file will be overwritten and
                                                 #any existing data will be overwritten

f.close() # always close file after using it for any method.