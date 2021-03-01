def open_file(filename):
    ''' Open the file and return the file object, if it does not exist return None '''
    try:
        return open(filename,'r')
    except FileNotFoundError:
        return None

def read_from_file_object(file:object):
    ''' Read from the file object and put it in a list and return it. '''
    all_file = []
    for line in file:
        all_file.append(line.split())
    return all_file

def fix_ints(all_file:list) -> list:
    ''' Change the numbers in the list from string to ints'''
    new_list = []
    current_list = []
    counter = 0
    for listi in all_file:
        for element in listi:
            try:
                current_list.append(int(element))
            except:
                current_list.append(element)
        new_list.append(current_list)
        current_list = []
    return new_list

def print_values(fixed_int_list:list):
    ''' Print all the values '''
    print(fixed_int_list[:2])


def main(filename):
    ''' Open the file and call the functions '''
    file_object = open_file(filename)
    if file_object == None:
        print(f"File {filename} not found")
        return
    all_file = read_from_file_object(file_object)
    fixed_int_list = fix_ints(all_file)
    print_values(fixed_int_list)

filename = input("Enter file name: ") 
main(filename)     