'''
Let's attempt to draw a sine wave using the print() statement.
Sine waves are usually drawn horizontally (left to right)
but the print() statement creates output that is ordered from top to bottom.
We'll therefore draw our wave vertically.

Our program shall accept two arguments:

    number_of_cycles - which controls how many waves should be drawn
    number_of_lines - which controls how many lines are used to print the waves

Python has a built in math.sin() function that we will leverage. To calculate its input,
we will consider the lines to be numbered from 0 and onwards.
The distance in radians is then given by:

radians_per_line = number_of_cycles * 2 * math.pi / number_of_lines
radians = line_number * radians_per_line

math.sin(radians) will return a number between -1.0 and 1.0 inclusive.
We are going to linearly transform the sine value to a number between 0 and 40 (inclusive) and
round that number to figure out how many "X" characters to print. Here are a few examples:

Sine value 	        Number of X characters to print
  -1.0 	                        0
   0.0 	                        20
   1.0 	                        40
   0.8414709848078965 	        37
'''

# Don't change the following lines
import math

number_of_cycles = float(input("Number of cycles: "))
number_of_lines = int(input("Stretched over how many lines? "))

radians_per_line = number_of_cycles * 2 * math.pi / number_of_lines

# ...now fill in the rest

for i in range(number_of_lines):
    radians = i * radians_per_line

    sin = math.sin(radians)

    # output = output_start + ((output_end - output_start) / (input_end - input_start)) * (input - input_start)
    output = 0 + ((40 - 0) / (1.0 - -1.0)) * (sin - -1.0)

    for x in range(round(output)):
        print("X", end="")

    print()