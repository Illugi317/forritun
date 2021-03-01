# palindrome function definition goes here
def checkpalindrome(in_str):
    #string = "".join(e for e in in_str if e.isalnum())
    #org = "".join(e for e in in_str if e.isalnum())
    string = ""
    for x in in_str:
        if x.isalnum():
            string += x
    revstring = string[::-1]
    if revstring.lower() == string.lower():
        return True
    return False
in_str = input("Enter a string: ")

check = checkpalindrome(in_str)
# call the function and print out the appropriate message

if check:
    print(f"\"{in_str}\" is a palindrome.")
else:
    print(f"\"{in_str}\" is not a palindrome.")
