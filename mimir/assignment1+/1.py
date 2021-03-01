'''
Write a program that, given seconds (int) as input, calculates hours, minutes, and seconds.

For example, given 80000 seconds as input, the program outputs:

22 hours, 13 minutes, and 20 seconds.

Hint 1: use integer division (//) and remainder (%)
'''

secs = int(input("Input seconds: ")) # do not change this line


hours = secs / 60 / 60
minutes = (secs / 60) % 60
seconds = secs % 60
print(int(hours),":",int(minutes),":",int(seconds)) # do not change this line