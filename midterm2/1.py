#Sum and Product

def calculate_sum(number:int):
    return int((int(number)*(int(number) + 1)/ 2))

def calculate_product(number:int):
    summa = 1
    for x in range(1,number+1):
        summa *= x
    return summa

def menu():
    print("1: Compute the sum of 1..n")
    print("2: Compute the product of 1..n")
    print("9: Quit")

def get_choice() -> int:
    try:
        choice = int(input("Choice: "))
        return choice
    except ValueError:
        return None
def number() -> int:
    try:
        number = int(input("Enter value for n: "))
        return number
        print(number)
    except:
        return None
#Driver code
choice = 0
while choice != 9:
    menu()
    choice = get_choice()
    if choice == None:
        continue
    elif choice == 9:
        continue
    elif choice == 1:
        number_n = number()
        if number_n == None:
            continue
        print(f"The result is: {calculate_sum(number_n)}")
    elif choice == 2:
        number_n = number()
        if number_n == None:
            continue
        print(f"The result is: {calculate_product(number_n)}")