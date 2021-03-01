'''
Write a Python program that reads a file, whose name is entered by the user, containing one sentence per line and prints out one token per line.  A token is defined as a sequence of any characters except white space.  There is a single white space between each token.

You are NOT allowed to use the split() function!

Let us assume that the file sentences.txt contains the following two sentences:

This is the first line.
And this is the second, a little bit longer.

Input/Output example:

This
is
the
first
line.
And
this
is
...
...
...
'''


def open_file(filename:str):
  try:
    return open(filename,"r")
  except:
    return None

# Main program starts here
filename = input("Enter filename: ")
file_obj = open_file(filename)
data = file_obj.read()

temp = ""
for char in data:
    if char != " ":
        temp += char
    else:
        temp += "\n"
print(temp)