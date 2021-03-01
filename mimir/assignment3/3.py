'''
Write a program using a while statement,
that given a series of numbers as input,
adds them up until the input is 10 and then prints the total.

Do not add the final 10.
'''

summ = 0

while True:
    num = int(input("Input an int: "))  # You can copy this line but not change it

    if num == 10:
        break

    summ += num

print(summ)