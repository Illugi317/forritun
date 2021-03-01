'''
Let a be a positive integer and consider the sequence where x0=a and
xn+1 = { xn/2, if xn is even
            3xn+1, if xn is odd }

The Collatz conjecture states that this sequence will always reach 1.

For example, if a=10 then x0=10, x1=5, x2=16, x3=8, x4=4, x5=2 and x6=1.

Write a program using a while loop that reads a positive integer from the user and
outputs each element of the above sequence until it reaches 1.
'''

a0 = int(input("Input a positive int: "))  # Do not change this line

x = a0

while True:

    print(int(x))

    if x % 2 == 0:
        x = x / 2

    else:
        x = 3 * x + 1

    if x == 1:
        print(int(x))
        break