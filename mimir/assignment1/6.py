'''
Write a Python program that:

    Accepts a five-digit integer as input
    Assign the variable first_three (int) to be the first three digits.
    Assign the variable last_two (int) to be the last two digits.
    Prints out the two computed values.

Hint: use quotient (//) and remainder (%)

For example, if the input is 12345, the output should be:

first_three: 123
last_two: 45

If the fourth digit is a zero, like 12305, the output should be:
first_three: 123
last_two: 5
(even though that is not strictly correct).
'''

n_str = input("Input n: ")
# remember to convert to an int
first_three = n_str[:3]
last_two = n_str[3:]
print("first_three:", int(first_three))
print("last_two:", int(last_two))
