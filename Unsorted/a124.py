def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True

def str_list_to_int(str_list: list):
    new_list = []
    for el in str_list:
        if not el.isdigit() or int(el) <= 0:
            return None

        new_list.append(int(el))

    return new_list

def get_prime_list(int_list):
    prime_list = []

    for el in int_list:
        if is_prime(el) and el not in prime_list:
            prime_list.append(el)

    return prime_list

def avg(int_list):
    return round(sum(int_list) / len(int_list), 2)

# The main program starts here
int_string = input("Enter integers separated with commas: ")
int_list = str_list_to_int(int_string.split(","))
if int_list is not None:
    print(f"Input list: {int_list}")
    int_list.sort()
    print(f"Sorted list:  {int_list}")
    prime_list = get_prime_list(int_list)
    print(f"Prime list:  {prime_list}")
    print(f"Min: {min(int_list)}, Max: {max(int_list)}, Average: {avg(int_list):.2f}")
else:
    print("Incorrect input!")