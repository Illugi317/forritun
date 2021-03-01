'''
Let us assume that Python does not have a multiplication operator.
Write a Python program that implements multiplication by using addition and a for loop.
'''

first = int(input("Input the first integer: "))
second = int(input("Input the second integer: "))

summ = 0

for i in range(first):
    for j in range(second):
        summ += 1

print(summ)