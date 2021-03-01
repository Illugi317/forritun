'''
Write a Python program that reads a file, whose name is input by the user, containing one word/token per line with an empty line between sentences.  The program prints out the longest word found in the file along with its length.

If the input file is not found (use try-except), the program should print "File not found".  Make sure, however, that the function which opens the file, does NOT do any printing.

Example input/output:

Enter filename: words.txt
Longest word is 'innflutningstolla' of length 17

The first few lines from words.txt looks like this:

Donald
Trump
forseti
Bandaríkjanna
tilkynnti
í
gærkvöldi
að
...
...
'''
# Your functions here
def open_file(filename:str):
  try:
    return open(filename,"r")
  except:
    return None

  
def find_longest(file_object:object):
  longest = 0
  longestword = ""
  for data in file_object:
    if len(data) > longest:
      longest = len(data)
      longestword = data.strip()
  return longestword
    
    
    
# Main program starts here
filename = input("Enter filename: ")
file_object = open_file(filename)
if file_object:
  longest_word = find_longest(file_object)
  print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
  file_object.close()
else:
  print("File not found")