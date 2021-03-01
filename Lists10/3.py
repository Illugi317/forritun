def begins_and_ends(word:str):
    return word[0] == word[-1] and len(word) > 1


listi = []
while True:
    new_word = input("Enter a word to be added to the list: ")

    if new_word == 'x':
        break
    listi.append(new_word)

print(listi)

for x in listi:
    if begins_and_ends(x):
        print(x)