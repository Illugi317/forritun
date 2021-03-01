def open_file(file_name): # Do not change this line
    '''Opens the given filename and returns its file object, or None if not found'''
    try:
        file_stream = open(file_name, "r")
        return file_stream
    except FileNotFoundError:
        return None

def read_matrix(file_object): # Do not change this line
    '''Creates an n-by-n integer matrix by reading data from file_object. 
    The matrix is a list of lists.'''
    matrix = []
    for line in file_object:
        numbers = [int(x) for x in line.split()]
        matrix.append(numbers)
    return matrix
    

def row_sum_same(matrix): # Do not change this line
    '''Returns the sum of the elements in each row of the matrix if the sum is the same, else 0'''
    sum_list = [] # create a list for all the sums
    for row in matrix:
        row_sum = sum(row)
        sum_list.append(row_sum)
    if len(set(sum_list)) == 1: # We change the sum list into a set, since sets remove duplicates we can then check if the length of the set is more than 1. 
        return sum_list[0]
    else:
        return 0
        
def col_sum_same(matrix): # Do not change this line
    '''Returns the sum of the elements in each column of the matrix if the sum is the same, else 0'''
    length = len(matrix)
    sum_list = [] #create a list for all the sums
    for col_num in range(0,length):
        col_list = [nested_list[col_num] for nested_list in matrix] # create a new list that includes only the col_num. We go through the matrix list and take each nested_list[col_num] for all the nested lists
        sum_list.append(sum(col_list))
    if len(set(sum_list)) == 1: # We change the sum list into a set, since sets removes duplicates we can then check if the length of the set is more than 1. 
        return sum_list[0]
    else:
        return 0

def print_matrix(matrix):
    ''' Print the matrix with a tab character inbetween and a newline after each row'''
    for nested_list in matrix:
        for num in nested_list:
            print(f"{num}\t",end="")
        print()

def main(): # Do not change this line
    ''' Main function, Get the filename from the user and call the functions in the corresponding order. If the file does not exist stop the program'''
    filename = input("File name: ") #"/home/star/HR/forritun/FINAL/test.txt"
    file_obj = open_file(filename)
    if file_obj is None:
        print(f"File not found")
        return
    matrix = read_matrix(file_obj)
    row_sum = row_sum_same(matrix)
    col_sum = col_sum_same(matrix)
    print_matrix(matrix)
    if row_sum == col_sum:
        print("Same sums")
    else:
        print("Not same sums")
# Main program starts here. Do not change it.
if __name__ == "__main__":
    main()