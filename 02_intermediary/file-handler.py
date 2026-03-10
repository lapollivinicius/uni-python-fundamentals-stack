# =========== function ============= #

# in py it's very important
# to know work file handle - create, read, update and delete files

# main method to this is
# we can pass some args with file

f = open('text.txt', 'r')

# MAIN ARGS
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - AddAppend - Opens a file for appending, creates the file if it does not exist
# "w" - OverWrite - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# ADDING
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# we can declare similar to function
with open("text.txt") as text:
  print(text.read())

# add a content - overwrite 
f.write("hello, world!")

# methods
# to read the content inside file
f.read(10) # return 10 first caracteres

# to read per lines
f.readline() 

# every open file needs be closed
f.close()

# to remove/delete a file we need a module
import os

# so we can use .remove to delete
os.remove('text.txt')



