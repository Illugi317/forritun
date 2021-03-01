'''
Write a Python program that takes a list L of integers > 0 as input and prints out the following information:

    The list L.
    The sorted version of L.
    A sorted list of the unique prime numbers in L.
    Minimum, maximum and average values in L. The average value should be printed with two decimal places (with trailing zeros if necessary).

You are allowed to use list functions, but you are not allowed to import any module.  The function is_prime() is given.

You need to print out an error message if the user enters invalid values into the list.  See an example below.

---

Example input/output:

Enter integers separated with commas: 2,5,7,2,8,10,34,23,9,4,5
Input list: [2, 5, 7, 2, 8, 10, 34, 23, 9, 4, 5]
Sorted list:  [2, 2, 4, 5, 5, 7, 8, 9, 10, 23, 34]
Prime list:  [2, 5, 7, 23]
Min: 2, Max: 34, Average: 9.91

 

Enter integers separated with commas: 1,2,b
Incorrect input!

Enter integers separated with commas: 1,2,-3
Incorrect input!
'''
def take_input():
    try:
        numbers = input("Enter integers separated with commas: ")
        return numbers.split(",")
    except:
        return None
def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True

def convert_num(numbers_list):
    try:
        for x in numbers_list:
            if int(x) >= 0:
                pass
            else:
                print("Incorrect input!")
                exit()
        return [int(x) for x in numbers_list]
    except:
        print("Incorrect input!")
        exit()
def check_prime(numbers):
    new_list = []
    for x in numbers:
        if is_prime(x):
            new_list.append(x)
    return new_list
def average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

numbers = take_input()
checked_numbers = convert_num(numbers)
rem_checked_numbers = list(dict.fromkeys(checked_numbers))
print(f"Input list: {checked_numbers}")
print(f"Sorted list:  {sorted(checked_numbers)}")
print(f"Prime list: {check_prime(sorted(rem_checked_numbers))}")
print(f"Min: {min(rem_checked_numbers)}, Max: {max(rem_checked_numbers)}, Average: {round((sum(checked_numbers)/len(checked_numbers)),2):.2f}")
