'''
Lets assume you are aquiring dollars each day.
On the first day you aquire one dollar,
two on the second, four on the third,
eight on the fourth and so on (doubling the number of dollars on each subsequent day).

How many days need to pass until you accumulate a certain target amount of dollars?

Write a Python program that accepts two inputs:

    The maximum number of days
    The dollar target

Then the program should use a for loop that finds how many days are needed in order to accumulate at least the dollar target.
If the limit can not be aquired in the given maximum number of days, the output should be 0.
'''

max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))

dollar_add = 1
summ = 0
days_when_amount_acquired = 0
# Fill in the missing code
for i in range(max_days):
    days_when_amount_acquired += 1

    summ += dollar_add

    if summ >= target:
        break

    dollar_add *= 2

else:
    days_when_amount_acquired = 0

print('Days needed:', days_when_amount_acquired)

