# Don't change these lines
number = int(input("Find the square root of integer: "))
guess = int(input("Initial guess: "))
tolerance = float(input("What tolerance: "))

# Implement the Babylonian square root algorithm
prev_guess = 0
count = 0
while abs(guess - prev_guess) > tolerance:
    count += 1
    prev_guess = guess
    guess = ((number/guess) + guess) / 2

# Don't change these lines
print("Square root of", number, "is", round(guess, 4))
print("Took", count, "reps to get it to tolerance")

