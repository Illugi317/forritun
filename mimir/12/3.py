'''
This program builds a wordlist out of all of the words found in an input file and prints all of the unique words found in the file in alphabetical order. Remove punctuations using 'string.punctuation' and 'strip()' before adding words to the wordlist.

Make your program readable!

Example input file test.txt:

the test file!
another line in the test file.
third, is this a good test?

Input/Output:

Enter filename: test.txt
['a', 'another', 'file', 'good', 'in', 'is', 'line', 'test', 'the', 'third', 'this']
'''
import re,string
def open_file(filename):
    try:
        return open(filename,'r')
    except:
        return None
new_string = string.punctuation
new_new_string = new_string.replace("-","")
regex = re.compile('[%s]' % re.escape(new_new_string))
def re(word):
    return regex.sub('',word)
word_list = []
filename = input("Enter filename: ")
file_object = open_file(filename)
for line in file_object:
    for char in line.split():
        word_list.append(char)
new_word_list = []
for word in word_list:
    new_word_list.append(re(word))
new_word_list = list(dict.fromkeys(new_word_list))
print(sorted(new_word_list))