# Fill in the missing code below
while True:
    rating = int(input("Input elo rating: ")) # Do not change this line
    if rating >= 2700:
        print("Super grandmaster") # Do not change this line
    elif rating < 100:
        break
    elif rating >= 2500:
        print("Grandmaster") # Do not change this line
    elif rating >= 2400:
        print("International") # Do not change this line
    elif rating < 1000:
        print("Invalid") # Do not change this line
    elif rating < 2400:
        print("Amateur") # Do not change this line
