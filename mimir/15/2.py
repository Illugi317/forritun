def take_input():
    try:
        numbers = input("Input a list of integers separated with a comma: ")
        return numbers.split(",")
    except:
        return None
def change_to_int(numbers):
    try:
        return [int(x) for x in numbers]
    except:
        return None
def get_set():
    return set()

def update_set(a_set,numbers):
    return a_set.update(numbers)

def print_menu():
    print("1. Intersection")
    print("2. Union")
    print("3. Difference")
    print("4. Quit")

def set_intersection(set_a,set_b):
    z = set_a.intersection(set_b)
    print(z)

def set_union(set_a,set_b):
    z = set_a.union(set_b)
    print(z)

def set_diff(set_a,set_b):
    z = set_a.difference(set_b)
    y = set_a.difference(set_a)
    final = z | y
    print(final)

def main():
    a = take_input()
    b = take_input()
    a_int = change_to_int(a)
    a_set = get_set()
    update_set(a_set,a_int)
    b_int = change_to_int(b)
    b_set = get_set()
    update_set(b_set,b_int)
    print(a_set)
    print(b_set)
    choice = ""
    while choice != 4:
        print_menu()
        choice = int(input("Set operation: "))
        if choice == 1:
            set_intersection(a_set,b_set)
        if choice == 2:
            set_union(a_set,b_set)
        if choice == 3:
            set_diff(a_set,b_set)
        if choice == 4:
            continue

main()