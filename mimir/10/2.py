'''
Write a program that makes a list of the unique letters in an input sentence.  That is, if the letter "x" is used twice in a sentence, it shouild only appear once in your list.  Neither punctuation nor white space should appear in your list.  The letters should appear in your list in the order they appear in the input sentence.

Example input/output:

Input a sentence: this is, a sentence.
Unique letters: ['t', 'h', 'i', 's', 'a', 'e', 'n', 'c']

Hint: import string

https://docs.python.org/3.8/library/string.html
'''
import string

# Implement a function here

def uni(sentence: str):
    listi = []
    for char in sentence:
        if char not in listi and char.isalpha():
            listi.append(char)
    return listi

# Main starts here
sentence = input("Input a sentence: ")
# Call the function here
unique_letters = uni(sentence)
print("Unique letters:", unique_letters)
