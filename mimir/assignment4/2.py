'''
Write a Python program using a for loop that,
given the number n as input,
prints all the numbers from 1 to n that are divisible by 3.
'''

highest = int(input("Input an int: "))

for i in range(1, highest + 1):
    if i % 3 == 0:
        print(i)

