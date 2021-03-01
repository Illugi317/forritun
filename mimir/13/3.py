def dict_to_tuples(a_dict):
    new_list = []
    for key, value in a_dict.items():
        new_list.append((key,value))
    return new_list

def add_to_dict(a_dict,key,value):
    a_dict[key] = value
    return

def remove_to_dict(a_dict, key):
    try:
        del a_dict['key']
    except KeyError:
        return None

def find_key(a_dict, key):
    find = a_dict.get(key)
    return find

def check_key(a_dict,key):
    if key in a_dict:
        return True
    else:
        return False

def execute_selection(choice, a_dict):
    if choice == 'a':
        key = input("Key: ")
        value = input("Value: ")
        check = check_key(a_dict,key)
        if check == True:
            print("Error. Key already exists.")
        else:
            add_to_dict(a_dict,key,value)
        
    elif choice == 'r':
        key = input("Key to remove: ")
        check = check_key(a_dict, key)
        if check == True:
            remove_to_dict(a_dict,key)
        else:
            print("Key not found.")
    elif choice == 'f':
        key = input("Key to locate: ")
        check = check_key(a_dict,key)
        if check == True:
            print(f"Value: {find_key(a_dict,key)}")
        else:
            print("Key not found.")
    else:
        print("Invalid choice.")

def menu_selection():
    print("Menu: ")
    choice = input("(a)dd, (r)emove, (f)ind: ")
    return choice

def main():
    more_input = True
    a_dict = {}
    
    while more_input:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more_input = again.lower() == 'y'
    
    tuple_list = dict_to_tuples(a_dict)
    print(sorted(tuple_list))

main()