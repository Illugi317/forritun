'''
You are cooking dinner. You found a delicious looking lasagne recipe.
There's only one problem. The recipe tells you to preheat your oven to 350 degrees Fahrenheit!
"What's that in sensible units?" you mutter to yourself. Let's write a program to find out!

Write a program that takes as input temperature in °F and converts it to °C.
Since your oven's temperature can only be set with one degree precision,
round the output to the nearest whole number (hint).
'''

degrees_f = int(input("Temperature in Fahrenheit: "))
# Convert degrees_f_str to an integer
degrees_c = round(((degrees_f -32) * 5) / 9)
# Convert to °C
# Round to nearest whole number
print("That's", degrees_c, "degrees Celcius")