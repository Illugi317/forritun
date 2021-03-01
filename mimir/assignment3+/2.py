'''
Write a program using a while statement,
that prints out the two-digit number such that when you square it,
the resulting three-digit number has its rightmost two digits the same as the original two-digit number.
That is, for a number in the form AB:

AB * AB = CAB, for some C.
'''

digit = 10
while digit < 100:
    summ = digit ** 2

    if digit == int(str(summ)[1:]):
        print(digit)

    digit += 1

