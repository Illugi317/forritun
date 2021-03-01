HOW_MANY_WINNING_NUMBERS = 5
WINNING_NUMBERS_INTERVAL = [1,40]

def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None

def get_lotto_nums(file_object:object):
    ''' Get a nested list of all numbers from the file '''
    lotto_nums = []
    for line in file_object:
        lotto_nums.append(line.split())
    return lotto_nums

def check_interval_on_num(num):
    ''' Check if the number is between the interval '''
    if WINNING_NUMBERS_INTERVAL[0] <= num <= WINNING_NUMBERS_INTERVAL[1]:
        return True
    else:
        return False

def check_winning_num(winning_num):
    ''' Check if the winning num is in the correct format '''
    list_of_num = winning_num.split()
    how_many = len(list_of_num)
    if how_many != HOW_MANY_WINNING_NUMBERS:
        return None
    for number in list_of_num:
        if number.isdigit():
            if not check_interval_on_num(int(number)):
                return None
        else:
            return None
    return True

def get_marked_number_list(lotto_list,winning_num):
    ''' Get marked list of lotto number according to the winning numbers '''
    marked_list = lotto_list
    for line_idx,line in enumerate(marked_list):
        for num_idx,number in enumerate(line):
            for winning_number in winning_num:
                if winning_number == number:
                    marked_list[line_idx][num_idx] += "*"
    return marked_list

def print_marked_list(marked_list):
    ''' Create the string to print and then print it '''
    string_to_print = ""
    for line in marked_list:
        string_to_print += " ".join(line) + "\n"
    print(string_to_print.rstrip())

def main(filename):
    ''' Open the file and call all the functions'''
    file_object = open_file(filename)
    if file_object == None:
        print(f"File {filename} not found!")
        return
    winning_num = input("Enter winning numbers: ")
    lotto_num_list = get_lotto_nums(file_object)
    check_format = check_winning_num(winning_num)
    if check_format == None:
        print(f"Winning numbers are invalid!")
        return
    marked_list = get_marked_number_list(lotto_num_list,winning_num.split())
    print_marked_list(marked_list)

filename =  input("Enter file name: ") #"/home/star/HR/forritun/aefingarprof/lotto.txt"
main(filename)     