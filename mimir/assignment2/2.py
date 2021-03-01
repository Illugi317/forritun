'''
Write a program that prompts for chess elo rating (an integer).
A valid rating is > 999.
A super grandmaster has rating >= 2700,
a grandmaster rating >= 2500, and an
international master has rating >= 2400.
Let's call a chess player with rating < 2400 amateur.
Write a program that prints out  "Super grandmaster", "Grandmaster", "International", "Amateur", or "Invalid",
depending on the input.
'''

rating = int(input("Input elo rating: ")) # Do not change this line
# Fill in the missing code below

if rating >= 2700:
    print("Super grandmaster") # Do not change this line
elif rating >= 2500:
    print("Grandmaster") # Do not change this line
elif rating >= 2400:
    print("International") # Do not change this line
elif rating > 999:
    print("Amateur") # Do not change this line
else:
    print("Invalid") # Do not change this line
