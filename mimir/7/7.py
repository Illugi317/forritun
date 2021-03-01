'''
Write a function that takes a string as an argument and returns a new string which contains every other character in the original string.

Also write a statement that calls the function with the given input as an argument.

Example input/output:
'''
def every_other_chr(a_str):
    '''Returns a new string containing every other character in a_str.'''
    return a_str[::2]
    
input_str = input("Enter a string: ")

print("Every other character:", every_other_chr(input_str))

'''
Write a function named count_digits that takes a string as an argument and returns the count of digits in the string. 

Also write a statement that calls the function with the given input as an argument.

Example input/output:
'''
# Your function definition goes here
def finddigit(input_str):
    counter = 0
    for x in input_str:
        if x.isdigit():
            counter += 1
    return counter

input_str = input("Enter a string: ")

# Call the function here
digit_count = finddigit(input_str)
print("No. of digits:", digit_count)

'''
Write a function named max_of_three that takes three numbers as arguments and returns the maximum of the three.

Also write a statement that calls the function using the given input as arguments.

'''
def max_of_three(first,second,third):  
    return(max(first,second,third))  
                                             
                                             
first = int(input("Enter first number: "))  
second = int(input("Enter second number: "))  
third = int(input("Enter third number: "))  
  
# Call the function here  
maximum = max_of_three(first,second,third)  
print("Maximum:", maximum)  

'''
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Write a function named is_prime that takes an integer argument and returns True if the number is prime and False otherwise. (Assume that the argument is an integer greater than 1, i.e. no need to check for erroneous input.)

Also write code that calls the function repeatedly from 2 to a number input by the user and prints out a message for each number saying whether it is a prime or not.

Example input/output:
Input an integer greater than 1: 10
2 is a prime
3 is a prime
4 is not a prime
5 is a prime
6 is not a prime
7 is a prime
8 is not a prime
9 is not a prime
10 is not a prime
'''
# is_prime function definition goes here                                      
def is_prime(n):                                                              
    for x in range(2,n):                                                                                                                      
        if n % x == 0:                                                                                                                        
            return False                                                                                                                      
                                                                      
    return True                                                       
                                                                      
max_num = int(input("Input an integer greater than 1: "))                                                                                     
# Call the function here repeatadly from 2 to max_num and print out the appropriate message  
for x in range(2,max_num+1):                                          
    a = is_prime(x)                                                   
    if a:                                                                                                                                     
        print(f"{x} is a prime")
    else:                                                           
        print(f"{x} is not a prime")

'''
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar. Sentence-length palindromes may be written when allowances are made for adjustments to capital letters, punctuation, and word dividers, such as

"Was it a car or a cat I saw?" or "No 'x' in Nixon".

Write a function that takes a string as an argument and returns True if the string is a palindrome and False otherwise.

Also write code that calls the function with the input as an argument and prints out the appropriate message.

Example input/output:

 

Enter a string: No 'x' in Nixon.
"No 'x' in Nixon." is a palindrome.

Enter a string: blabla
"blabla" is not a palindrome.
'''
# palindrome function definition goes here                              
def checkpalindrome(in_str):                                            
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

'''
Write a function, valid_date, that accepts a string representing a date, and returns True if the date is valid, otherwise False.

A valid date has the format "dd.mm.yy", and satisfies the following properties:

    It contains exactly 8 characters
    A period is the separator between the day and the month part
    The day part must be between 01 and 31
    The month part must be between 01 and 12
    The year part must be between 00 and 99

Example input/output:
'''
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
