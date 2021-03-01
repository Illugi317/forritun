'''
Here is a simple logic circuit that has 3 inputs (A, B and C) and 1 output (D)


Write a program that is equivalent to the logic circuit above.
It should accept three subsequent integer values (either 0 or 1) as input for A, B and C respectively.
It should then print either 0 or 1, depending on the value of D.

Hint: Page 147 in the textbook has truth tables for the AND, OR and NOT logical operators.
'''

a = bool(int(input("A")))
b = bool(int(input("B")))
c = bool(int(input("C")))

# compute d
d = (a and not b) or (not a and c)

print("D is", int(d))