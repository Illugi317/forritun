def factorial(n_str):
    summa = 1
    for x in range(1,int(n_str)+1):
        summa *= x   
    return summa

def sum_natural(n_str):
        return int((int(n_str)*(int(n_str) + 1)/ 2))
def sum_fibonacci(n_str):
    summa = 0
    number1,number2 = 0,1
    for iteration in range(int(n_str)):
        summa += number1
        number3 = number1 + number2
        number1 = number2
        number2 = number3
    return summa

def approximate_euler(n_str):
    summa = 0
    for x in range(int(n_str)):
        summa += (1/factorial(x))
    return round(summa,5)

def options():
    print("Please choose one of the options below:")
    print("a. Display the sum of the first N natural numbers. ")
    print("b. Display the sum of the first N Fibonacci numbers. ")
    print("c. Display the approximate value of e using N terms.")
    print("x. Exit from the program.\n")
option_str = "abc"
options()
while True:
    choice_str = input("Enter option: ")
    if choice_str == "x":
        break
    elif choice_str not in option_str :
        print(f"Unrecognized option {choice_str}\n")
        options()
        continue
    n_str = input("Enter N: ")
    if n_str.isnumeric() and int(n_str) >= 2:
        if choice_str == "a":
            print(f"Natural number sum: {sum_natural(n_str)}")
        elif choice_str == "b":
            print(f"Fibonacci sum: {sum_fibonacci(n_str)}")
        elif choice_str == "c":
            print(f"Euler approximation: {approximate_euler(n_str)}")
    else:
        print(f"Error: {n_str} was not a valid number.\n")

