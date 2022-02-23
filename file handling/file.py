'''
   python file handling is a built in module that contain many other functions to perform operation on files
'''

# open()        used to open a file , take two arguments : filename and mode.
# read()        used to read the entire file content.
# readline()    used to read one line in a file.
# readlines()   used to read file and returns a list of lines.
# write()       used to write to a file.
# writelines()  used to write a list of strings.
# append()      used to append to existing file.
# close()       used to close file when you are done.

# python file access modes
#r   default mode. used for reading.
#r+  opens for reading and writing to file.
#w  opens a file for writing,creates the file if not present.
#w+ opens file for writing and reading.
#rb  for reading a binary file eg images and video file(non text)
#a   opens file to append. creates a new file if not present.
#t  text-default mode.
#x  create the specified file, returns error if the file exist.