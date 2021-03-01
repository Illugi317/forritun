'''
Let's write a program that plays a guessing game.
This program will ask its user to pick a number between 1 and 100 (inclusive) and then proceed to guess what it is.
The user tells the computer whether each guess is too high, too low or correct.

The program will use a method similar to binary search,
halving the range of possible solution every time the user answers either 'low' or 'high'.
Using this method, our program is guaranteed to guess correctly using at most 7 guesses!

When the game begins, the solution must lie somewhere between 1 and 100.
To divide the solution space in half, we pick a guess that is exactly in the middle; 50.
Imagine that the user says that this is too high. Then the solution must lie between 1 and 49.
Our next guess will therefore be 25.

If the user says this is too low,
then the correct solution must lie between 26 and 49 so our next guess will therefore be 37

By repeating this process up to 7 times, we are guaranteed to find the correct answer. If not, then the user must be cheating!

The starter code below already contains most of the print and input statements needed.
You can therefore concentrate on the actual game logic.
Requirements

    When the user types in "c", then the program should print "I AM VICTORIOUS" and then stop.
    When the user types in "q", then the program should print "Quitter" and then stop.
    If the program detects that the user is trying to cheat then it should print "Tsk, tsk, don't try to cheat me" and then stop.
    The program should always pick a guess that is in the middle of the range of possible solutions, rounded down (floored) to the nearest integer.

'''

# These lines you can keep as is
print("Think of a number between 1 and 100 (inclusive)")
print("I am going to guess what it is")
input("Press enter when you are ready to play")

# Here you might want to initialize some variables

guess = 50

lowest = 1
highest = 100

counter = 1
# Then start a while loop
while True:

    # These lines you can keep as is
    print("Is the number", guess, "?")
    print("Type one of the following letters and press enter:")
    print("h: if the guess is too (h)igh")
    print("l: if the guess is too (l)ow")
    print("c: if the guess is (c)orrect")
    print("q: to (q)uit the game")

    if (counter > 7 or lowest == highest) and guess != 100:
        # If you detect that the user has not been truthful, you should print the following
        print("Tsk, tsk, don't try to cheat me")
        break

    cmd = input()

    if cmd == "q":
        print("Quitter")
        break

    elif cmd == "c":
        print("I AM VICTORIOUS")
        break

    elif cmd == "h":
        highest = guess - 1

        guess = (lowest + highest) // 2

    elif cmd == "l":
        lowest = guess + 1
        guess = (lowest + highest) // 2

    counter += 1

