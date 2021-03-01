'''
Write a Python program using nested for loops that,
given an integer n as input,
prints all consecutive sums from 1 to n.
'''

num = int(input("Input an int: "))  # Do not change this line

for i in range(1, num + 1):
    summ = 0

    for j in range(1, i + 1):
        summ += j

    print(summ)