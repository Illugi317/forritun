ISBN_FORMAT = "X-XXX-XXXXX-X"
ISBN_SEP = "-"
ISBN_DIGIT_COUNT = ISBN_FORMAT.count("X")

def check_for_digits(isbn_string):
    ''' Check if the the string only contains digits and has the equal number of digits '''
    element_list = isbn_string.split(ISBN_SEP)
    fixed_str = "".join(element_list)
    if len(fixed_str) != ISBN_DIGIT_COUNT:
        return None
    for x in fixed_str:
        if not x.isdigit():
            return None
    return True

def check_pos(idx,counter):
    '''Check if the string holds up to the format, idx is the where in the list we are and counter is how many numbers are in there '''
    splitted = ISBN_FORMAT.split(ISBN_SEP)
    to_check = splitted[idx-1]
    how_many = len(to_check)
    if how_many != counter:
        return False
    else:
        return True

def check_format(checked_isbn_string):
    ''' Check the format of the isbn strign '''
    split_counter = 0
    how_many_digits = 0
    for char in checked_isbn_string:
        if char == ISBN_SEP:
            split_counter += 1
            correct = check_pos(split_counter,how_many_digits)
            if not correct:
                return None
            how_many_digits = 0
            continue
        how_many_digits += 1
    return True

def main():
    '''Main program'''
    isbn_string = "continue"
    while isbn_string != "q":
        isbn_string = input("Enter an ISBN: ")
        if isbn_string == "q":
            continue
        decimal_check = check_for_digits(isbn_string)
        format_check = check_format(isbn_string)
        if decimal_check == None or format_check == None:
            print("Invalid format!")
            continue
        print("Valid format!")

main()