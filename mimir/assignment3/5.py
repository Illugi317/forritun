'''
Write a program that prompts repeatedly for chess elo rating (an integer) until the rating < 1 is entered.
A super grandmaster has rating >= 2700,
a grandmaster rating >= 2500, and an
international master has rating >= 2400.
Let's call a chess player with rating < 2400 amateur, but a rating < 1000 is invalid.
Write a program that repeatedly prints out
"Super grandmaster",
"Grandmaster",
"International",
"Amateur", or
"Invalid", depending on the input.
'''

rating = 1
while rating > 0:
    rating = int(input("Input elo rating: "))  # Do not change this line
    # Fill in the missing code below

    if rating >= 2700:
        print("Super grandmaster")  # Do not change this line

    elif rating >= 2500:
        print("Grandmaster")  # Do not change this line

    elif rating >= 2400:
        print("International")  # Do not change this line

    elif rating >= 1000:
        print("Amateur")  # Do not change this line

    elif 0 < rating < 1000:
        print("Invalid")  # Do not change this line

