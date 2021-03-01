'''
Write a program using a while statement,
that given an integer as the input,
prints all the factors of that number, one in each line.
'''

n = int(input("Input an int: "))  # Do not change this line
factor = 1
# Fill in the missing code below

while factor <= n:
    if n % factor == 0:
        print(factor)

    factor += 1