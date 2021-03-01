'''
You likely learned the Euclidean distance formula in high school -- the formula to find the distance between two points in a plane.  You will take the two integer coordinates as input and output the distance between them.

Hint: You can use the sqrt function in the math module.
'''

import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line

# convert strings to ints
x1 = int(x1_str)
y1 = int(y1_str)
x2 = int(x2_str)
y2 = int(y2_str)

d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

#  d =
print("d =",d)  # do not change this line