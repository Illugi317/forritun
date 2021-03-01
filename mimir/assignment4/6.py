'''
Write a Python program, using a for loop, that prints the following series and computes its sum,

2, -4, 6, -8, 10, ...

The user inputs the length of the series.
'''

length = int(input("Input the length of series: "))

summ = 0
num = 2
for i in range(length):
    summ += num

    print(num)

    if num < 0:
        num -= 2
    elif num > 0:
        num += 2

    num = -num

print("Sum:", summ)