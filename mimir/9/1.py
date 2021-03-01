'''

Write a program that reads a file, whose name is input by the user, and prints out the contents after removing all spaces and newlines. Punctuations will be preserved.

For example, if the input file contains:

   This is a test file, for chapter 06.
       This a new line in the file!

Then, your program's output will show:

Thisisatestfile,forchapter06.Thisanewlineinthefile!

Hint:

Consider using the strip() and replace() functions.
'''
# Main starts here
file_name = input("Enter filename: ")

data = open(file_name,"r").read().replace(" ","").replace("\n","")
print(data, end="")