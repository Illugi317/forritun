'''
A prime number is a whole number greater than 1 whose only factors are 1 and itself.

Write a program using a while statement,
that given an int as the input, prints out "Prime" if the int is a prime number,
otherwise it prints "Not prime".
'''

n = int(input("Input a natural number: "))  # Do not change this line

factor = 2

prime = False

# Fill in the missing code below
while factor < n:
    if n % factor == 0:
        prime = False
        break

    factor += 1

else:
    if n != 1:
        prime = True

# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")