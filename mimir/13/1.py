'''Write a program that asks for a name and a phone number from the user and stores the two in a dictionary as key-value pair.

The program then asks if the user wants to enter more data (More data (y/n)? ) and depending on user choice, either asks for another name-number pair or exits.  Finally, it stores the dictionary <key, values> pairs in a list of tuples and prints a sorted version of the list.

Note: If a name is already in the dictionary, the old value should be overwritten.

Example:

Name: pranshu
Number: 517-244-2426
More data (y/n)? y
Name: rich
Number: 517-842-5425
More data (y/n)? y
Name: alireza
Number: 517-432-5224
More data (y/n)? n
[('alireza', '517-432-5224'), ('pranshu', '517-244-2426'), ('rich', '517-842-5425')]'''

def add_to_dict(my_dict: dict, name: str, number: str):
    my_dict[name] = number

def print_dict(my_dict) -> list:
    new_list = []
    for key, value in sorted(my_dict.items()):
        new_list.append((key,value))
    return new_list

my_dict = dict()

while True:
    name = input('Name: ')
    number = input('Number: ')
    add_to_dict(my_dict,name,number)
    more = input('More data (y/n)? ')
    if more == 'y':
        continue
    if more == 'n':
        print(print_dict(my_dict))