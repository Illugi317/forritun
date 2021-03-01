'''

Write a program that accepts a list of integers, int_list, as an argument and a single integer, check_int, and then prints 'True' if two consecutive values of check_int are found in the int_list. 

The program prints out an error message saying 'Error: enter only integers.' if the list is found to contain any non-numeric characters. 

Examples:

Enter elements of list separated by commas: 2,3,4,4,5,6
Consecutive check: 4
True

Enter elements of list separated by commas: 2,3,4,5,6
Consecutive check: 4
False

Enter elements of list separated by commas: 2,3,5,8,8,x
Error: enter only integers.
'''
def take_input():
    try:
        numbers = input("Enter elements of list separated by commas: ")
        return numbers.split(",")
    except:
        return None
def check(numlist):
    for x in numlist:
        if x.isnumeric():
            pass
        else:
            return False
    return True

numbers = take_input()
check = check(numbers)
if check is False:
    print("Error: enter only integers.")
    exit()

check_int = input("Consecutive check: ")
count = 0
for x in numbers:
    if x == check_int:
        count += 1

if count >= 2:
    print("True")
else:
    print("False")
