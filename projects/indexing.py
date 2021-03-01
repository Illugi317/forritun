email_address = input("Email address: ")
print("Checking...")
index = 0
splited = email_address.split('@')
if '@' not in email_address:
    print("@ symbol is missing")
elif email_address.count('@') > 1:
    print(email_address)
    sec_at = email_address.find('@',email_address.find('@') + 1)
    print(" " * sec_at + "^--there's an extra @ symbol here")
elif splited[0] == "":
    print(" " + email_address)
    print("^--this bit is missing")
elif splited[1] == "":
    print(email_address)
    print(" " * len(email_address) + "^--this bit is missing")
elif email_address[0] == ".":
    print(email_address)
    print("^--there's a dot here that probably shouldn't")
elif email_address[email_address.find('@') - 1] == ".":
    print(email_address)
    print(" " * (email_address.find('@') - 1) + "^--there's a dot here that probably shouldn't")
elif ".." in email_address:
    print(email_address)
    print(" " * email_address.find("..") + "^--there are consecutive dots here")
elif "." not in splited[1]:
    print(f"The top-level-domain is missing. Did you perhaps intend to write {email_address}.com?")
else:
    print("Seems legit")
