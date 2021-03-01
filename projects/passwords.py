# Skilgreina breytur
invalid_tries = 0
valid_tries = 0
tries = 0
# Skilgreina constants
MAX_LENGTH = 20
MIN_LENGTH = 6

# Skilgreina skilyrði sem þarf að uppfylla til að passwordið gengur upp.
one_upper = bool
one_lower = bool
one_num = bool
while True:
    one_upper = False
    one_lower = False
    one_num = False
    password = input("Enter a new password: ")
    if password == "q":
        break
    tries += 1
    length_of_password = len(password)
    if length_of_password < MIN_LENGTH or length_of_password > MAX_LENGTH:
        print("Invalid length")
        pass
    else:
        for char in password:
            if char.isupper():
                one_upper = True
            elif char.islower():
                one_lower = True
            elif char.isnumeric():
                one_num = True


        if not one_lower:
            print("At least one lower case letter needed")
        if not one_upper:
            print("At least one upper case letter needed")
        if not one_num:
            print("At least one number needed")
    
    if one_upper and one_lower and one_num:
        valid_tries +=1
        print("Valid password of length",length_of_password)
    else:
        invalid_tries += 1
print(f"You tried {tries} passwords, {valid_tries} valid, {invalid_tries} invalid")
