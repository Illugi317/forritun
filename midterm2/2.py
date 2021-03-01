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
    '''Change the numbers in the list from string to ints '''
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

def separate_lists(all_file_int_list:list) -> list:
    '''Seperate the boy and girl names into separate lists '''
    boys_list = []
    girls_list = []
    for nested in all_file_int_list:
        boys_list.append([nested[1],nested[2]])
        girls_list.append([nested[3],nested[4]])
    return boys_list,girls_list

def get_frequency(boys_list:list, girls_list:list) -> list:
    '''Get the frequency from both lists and put them in seperated lists.'''
    boys_freq_list = []
    girls_freq_list = []
    [boys_freq_list.append(ele[1]) for ele in boys_list]
    [girls_freq_list.append(ele[1]) for ele in girls_list]
    return boys_freq_list,girls_freq_list

def get_50_percentile(freq_list:list) -> list:
    ''' Calculate the 50'th percentile '''
    sorted_list = sorted(freq_list)
    sum_of_list = sum(freq_list)
    counter = 0
    summa = 0
    res = 0
    for ele in sorted_list[::-1]:
        summa += ele
        counter += 1
        if summa > sum_of_list/2:
            return counter

def print_values(fixed_int_list:list,boys_list:list,girls_list:list,freq_boys:list,freq_girls:list):
    ''' Print all the values '''
    print(fixed_int_list[:2])
    print(boys_list[:5])
    print(girls_list[:5])
    print(f"Total frequency of boy names: {sum(freq_boys)}")
    print(f"Total frequency of girl names: {sum(freq_girls)}")
    print(f"50th percentile rank for boys: {get_50_percentile(freq_boys)}")
    print(f"50th percentile rank for girls: {get_50_percentile(freq_girls)}")


def main(filename):
    ''' Open the file and call all the functions'''
    file_object = open_file(filename)
    if file_object == None:
        print(f"File {filename} not found!")
        return
    all_file = read_from_file_object(file_object)
    fixed_int_list = fix_ints(all_file)
    boys_list, girls_list = separate_lists(fixed_int_list)
    freq_boys,freq_girls = get_frequency(boys_list, girls_list)
    print_values(fixed_int_list,boys_list,girls_list,freq_boys,freq_girls) 

filename = input("Enter file name: ")#"/home/star/HR/forritun/midterm2/baby.txt"
main(filename)     