# These lines you can keep as is
print("Think of a number between 1 and 100 (inclusive)")
print("I am going to guess what it is")
input("Press enter when you are ready to play")

# Here you might want to initialize some variables
gmax = 100
guess = 50
gmin = 1
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
    if (counter > 7 or gmin == gmax) and guess != 100:
        print("Tsk, tsk, don't try to cheat me")
        break
    cmd = input()
    counter += 1
    # Now it's up to you to check the command and take appropriate action
    if cmd == "q":
        print("Quitter")
        break
    if cmd == "h":
        gmax = guess - 1
        guess = (gmin+gmax) // 2
    if cmd == "c":
        print("I AM VICTORIOUS")
        break
    if cmd == "l":
        gmin = guess + 1
        guess = (gmin+gmax) // 2

# If you detect that the user has not been truthful, you should print the following
                    