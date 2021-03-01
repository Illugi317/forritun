'''
Write a program that keeps asking the user for new words to be added to a list until the user enters 'x' ('x' should NOT be added to the list).  This list is printed out.

After that, the program creates a new list with the words, of length > 1, from the original list that begin and end with the same character. Finally, the program prints out all of the words in the new list, one per line.

Example input/output:

Enter word to be added to list: mam
Enter word to be added to list: he
Enter word to be added to list: would
Enter word to be added to list: wow
Enter word to be added to list: I
Enter word to be added to list: like
Enter word to be added to list: not
Enter word to be added to list: abba
Enter word to be added to list: x
['mam', 'he', 'would', 'wow', 'I', 'like', 'not', 'abba']
mam
wow
abba
'''
def begins_and_ends(word:str):
    return word[0] == word[-1] and len(word) > 1


listi = []
while True:
    new_word = input("Enter word to be added to list: ")

    if new_word == 'x':
        break
    listi.append(new_word)

print(listi)

for x in listi:
    if begins_and_ends(x):
        print(x)