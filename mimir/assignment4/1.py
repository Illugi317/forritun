'''
Write a Python program using a for loop that, given an integer as input,
prints all the integers starting from 1 up to but not including that number.
Print one number per line.
'''

upto = int(input("Input an int: "))  # Do not change this line

for i in range(1, upto):
    print(i)