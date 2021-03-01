'''
Let's implement the Babylonian square root algorithm. Here's a pseudocode description of the algorithm.

    let n be the number for which to find the square root
    let g be the initial guess
    let t be the tolerance
    let g' be our previous guess, initialized to 0
    while the absolute difference between g and g' is greater than t
      g' = g
      g = average of n/g and g

The program shall take as input the following

    number - an integer for which to find the square root
    guess  - an integer representing from where to start the search for the actual square root
    tolerance - a float indicating the minimum change between iterations until the algorithm stops

It should print out the square root, rounded to the 4th decimal, and the number of repetitions until tolerance was reached.
'''

# Don't change these lines
number = int(input("Find the square root of integer: "))
guess = int(input("Initial guess: "))
tolerance = float(input("What tolerance: "))

previous_guess = 0

count = 0
# Implement the Babylonian square root algorithm
while abs(guess - previous_guess) > tolerance:
    count += 1

    previous_guess = guess

    guess = ((number / guess) + guess) / 2

# Don't change these lines
print("Square root of", number, "is", round(guess, 4))
print("Took", count, "reps to get it to tolerance")
