'''
Your nation's prestigious reputation is being tarnished by the evil foreign media due to a slight mishap in one of its nucelar power plants.
To prevent this from happening again,
the wise leaders of your nation have given you the task to create a computer program that controls reactor temperature.
At regular intervals, the temperature of the water in the reactor is measured.
The last two measurements are given to the program (as integers) which then decides what should be done with the control rods in order to maintain an optimum operating temperature of 300°C.
The control logic is as follows:

    If the current temperature is below 300°C and the temperature is not rising then raise the control rods to increase temperature.
    If the current temperature is below 300°C but the temperature is rising then keep the control rods where they are.
    If the current temperature is exactly 300°C then keep the control rods where they are.
    If the current temperature is above 300°C and the temperature is not falling then lower the control rods to reduce temperature.
    If the current temperature is above 300°C but the temperature is falling then keep the control rods where they are.
    If the current temperature is 350°C or higher then initiate emergency shutdown procedures.

Depending on the pair of measurements, the program should print one of the following strings:

    "raise"
    "keep"
    "lower"
    "shutdown"

'''

temp_now = int(input("Current temperature (C°): "))
temp_prev = int(input("Previous temperature (C°): "))

RAISE = "raise"
KEEP = "keep"
LOWER = "lower"
SHUTDOWN = "shutdown"

# ... implement control logic and print the appropriate action
if temp_now >= 350:
    print(SHUTDOWN)
elif temp_now < 300 and temp_now <= temp_prev:
    print(RAISE)
elif temp_now < 300 and temp_now > temp_prev:
    print(KEEP)
elif temp_now == 300:
    print(KEEP)
elif temp_now > 300 and temp_now >= temp_prev:
    print(LOWER)
elif temp_now > 300 and temp_now < temp_prev:
    print(KEEP)