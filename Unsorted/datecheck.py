# Your function definition goes here
def valid_date(date_str):
    LENGTH = 8
    date_split = "".join(date_str.split(".")).isdigit()
    if len(date_str) > LENGTH or len(date_str) < LENGTH:
        return False
    elif date_split == False:
        return False
    elif date_str[2] != "." or date_str[5] != ".":
        return False
    elif int(date_str[0:2]) < 1 or int(date_str[0:2]) > 31:
        return False
    elif int(date_str[3:5]) < 1 or int(date_str[3:5]) > 12:
        return False
    elif int(date_str[6:7]) < 0:
        return False
    else:
        return True

        
date_str = input("Enter a date: ")
if valid_date(date_str):
    print("Date is valid")
else:
    print("Date is invalid")  
