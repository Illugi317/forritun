'''
Write a program that prompts the user for a sentence and then:

    Collects the individual characters of the sentence into a list
    Prints the list
    Prints the list sorted

Example input/ouptut:

Input a sentence: I love programming
['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
[' ', ' ', 'I', 'a', 'e', 'g', 'g', 'i', 'l', 'm', 'm', 'n', 'o', 'o', 'p', 'r', 'r', 'v']
'''

# The main program starts here
sentence = input("Input a sentence: ")
print(list(sentence))
print(sorted(list(sentence)))