ALLOWED_DECIMALS = 4


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
        all_file.append(line.strip())
    return all_file

def print_sequence(name_of_sequence:str, number_list:list):
    ''' Print the name of the list and the list itself, if there is nothing in the list print nothing i.e. string = "". mimir wants an extra space after printing the list so i added it '''
    extra_space = str
    if len(number_list) != 0:
        extra_space = " "
    else:
        extra_space = ""

    print(f"\t{name_of_sequence}")
    print(f"\t\t{' '.join(number_list)}{extra_space}")

def print_one(name:str, number:float):
    ''' Print the string and also print the median value, if the value is None print nothing but he tabs'''

    if number == None:
        print(f"\t\t")
    else:
        print(f"\t\t{number}")

def float_to_string(number_list):
    ''' Simple list expression to return a list full of strings to print out. '''
    return [str(a) for a in number_list]

def cumulative_sum(checked_list: list):
    ''' Find the cumulative sum and put it one by one in a list and return the list.  '''
    summa = 0
    cumulative_sum_list = []
    for ele in checked_list:
        summa += ele
        cumulative_sum_list.append(round(summa,ALLOWED_DECIMALS))
    return cumulative_sum_list
   
def get_median_value(number_list):
    '''  Calculate the median value, if the length is 0 then return None.
    Check if the length of the list is even or odd number. 
    and then calculate it depending on what the length of the list is.'''
    if len(number_list) == 0:
        return None
    idx = ((len(number_list) / 2) - 1)
    if len(number_list)%2 == 0:
        median = (number_list[int(idx)] + number_list[int(idx)+1]) / 2
    else:
        median = number_list[int(idx+1)]
    return round(median,ALLOWED_DECIMALS)

def process_one_file(filename:str):
    ''' Process one file from the file list. '''
    file_object = open_file(filename)
    if file_object == None:
        print(f"File {filename} not found")
        return
    print(f"File {filename}")
    file_list = read_from_file_object(file_object)
    checked_file_list = check_list(file_list)
    cumulative_sum_list = cumulative_sum(checked_file_list)
    print_sequence("Sequence:",float_to_string(checked_file_list))
    print_sequence("Cumulative sum:",float_to_string(cumulative_sum_list))
    print_sequence("Sorted sequence:",float_to_string(sorted(checked_file_list)))
    print_one("Median:", get_median_value(sorted(checked_file_list)))
    

def process_all_files(filename_list:list):
    ''' Simple for loop to process each file and print out the results '''
    for filename in filename_list:
        print()
        process_one_file(filename)


# Main program starts here
filename_list = input("Enter filenames: ").split()
process_all_files(filename_list)