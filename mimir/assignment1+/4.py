'''
You are painting your roof. You have a 10 liter can of paint that's full to the brim.
That poses a bit of a problem because you can't put it down on the roof because it's tilted,
otherwise paint will spill out of the can. You decide to build a simple platform on which to place the can of paint.
You already have one piece of plywood that's sized at 50cm x 50 cm.
Your going to screw another piece of wood at a right angle at the end of it to make the platform perfectly level while placed on the roof.
You have a cool app on your phone that allows you to measure the roof's angle in degrees (denoted as Θ in the diagram).
Now it's time to put your programming skills to use to calculate the exact height of the second piece.


Hint: the math module in Python contains commonly used trigonometric functions.
'''

import math
length_cm = 50
degrees = int(input("Roof's angle in degrees: "))
# Convert input to integer
# Convert degrees to radians in order to use the trigonometric functions in the math module

horn = 180 - 90 - degrees


height_cm = length_cm / math.tan(math.radians(horn))


# Calculate the the height of the triangle
print("To make the platform level, the height must be", round(height_cm, 1), "cm")