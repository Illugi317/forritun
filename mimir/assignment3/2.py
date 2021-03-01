'''
Write a program using a while statement,
that given the number n as input,
prints the first n even numbers starting from 2.
'''

num = int(input("Input an int: "))  # Do not change this line

even_num = 2
# Fill in the missing code below
while num > 0:
    print(even_num)

    num -= 1
    even_num += 2