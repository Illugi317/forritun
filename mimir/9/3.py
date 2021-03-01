'''
Write a program that prompts for two numbers.  Then call a function divide_safe(num1_str, num2_str), which returns the result of dividing the first number by the second numer.  If the given strings do not represent numbers or the second number is 0, the function returns None. Use try-except and catch two types of exceptions: ValueError and ZeroDivisionError.

The main program prints the result rounded to 5 decimal digits if no error occured, else prints None.

Input/Output example:

Input first number: 2.3
Input second number: 6.5
0.35385
'''
def divide_safe(num1_str: str, num2_str: str):
    try:
        return round(float(num1_str)/float(num2_str),5)
    except:
        return None

num1_str = input('Input first number: ')
num2_str = input('Input second number: ')

result = divide_safe(num1_str, num2_str)
print (result)