ALLOWED_DECIMALS = 2

def open_file(filename:str)-> object:
    ''' Op1en the file and return the file object, if it does not exist return None '''
    try:
        return open(filename,'r')
    except FileNotFoundError:
        return None

def convert_str_to_float(numbers_list:list) -> list:
    ''' Convert a list of string numbers to a list of float numbers '''
    return [float(x) for x in numbers_list]

def calculate_weighted_grade(parts_list:list, student_list:list) -> int:
    ''' Calculate the course grade for each student, by taking the weight of each grade and multiplying it by the grade the student got, then adding them up to a final grade    '''
    course_grade = 0
    for num in range(len(parts_list)): #Iterate x times where x is the number of parts
        weight = parts_list[num][1]
        grade = student_list[1][num]
        course_grade += weight * grade
    return course_grade

def add_to_student_list(course_grade:int,student:int,student_list):
    ''' Add the course grade to the end of the current student_list. Use (element,) to add to a tuple '''
    student_list[student] = student_list[student]+(course_grade,)

def parse_file_parts(file_object:object) -> list:
    ''' Parse the file parts, no need for a for loop to iterate over the file, since the file is always 2 lines long'''
    file_list = file_object.read().split('\n') #Split at the new line to get both lines as string.
    numbers_list = convert_str_to_float(file_list[1].split()) #Convert the weights to float value
    names_list = file_list[0].split() 
    combined_list = []
    for element in range(len(numbers_list)):
        combined_list.append((names_list[element],numbers_list[element])) #Combine both the lists one element per tuple
    return combined_list


def parse_file_students(file_object:object) -> list:
    ''' Parse the student file, read all the lines, split on newline character and that is a student_email and their grades.'''
    file_list = file_object.readlines()
    student_list = []
    for element in file_list:
        split_elements = element.strip('\n').split('  ') #Split on the newline and double space to get the emails and grades seperated in a list
        emails = split_elements[0]
        grades = convert_str_to_float(split_elements[1].split()) #Grades are splitted and then converted to floats.
        student_list.append((emails,grades))
    return student_list

def get_student_values(student_list:list) -> list:
    ''' Get get student emails and student grades [9.2, 2.1, 5.3, 5.1, 7.7] and add the course final grade to the list '''
    grades_list = []
    for student in student_list:
        temp_list = student[1]
        temp_list.append(round(student[2],ALLOWED_DECIMALS))
        temp_list = [student[0]] + temp_list
        grades_list.append(temp_list)
    return grades_list


def get_formated_results(grades_list,parts_list:list) -> list:
    ''' Create a formatted list to read from when printing out the results in a pretty manner. Note*: Need to add 'Course grade' to the end of the list by using append and then add 'Student ID' by using plus '''
    results = []    
    part_list = []
    for element in parts_list:
        part_list.append(element[0])
    part_list.append('Course grade')
    part_list = ['Student ID'] + part_list
    results = [part_list] + grades_list
    return results
    

def pretty_print(formated_list:list):
    ''' Print the weights names and grades in a pretty manner use enumerate to use find out when printing the first item with 16 spaces and then the rest with 14 spaces'''
    line_to_print = '\n'
    for line in formated_list: 
        for idx, item in enumerate(line):
            if idx == 0:
                line_to_print += f"{item:>16}" #Use {0:16}, this forces 16 spaces before the element
            else:
                line_to_print += f"{item:>14}" #Use {0:14}, this forces 14 spaces before the element
        line_to_print += '\n'
    return line_to_print

def calculate_and_print(parts_list,student_list):
    ''' Add to  the student_list the course_grade without creating a new list and call the corresponding functions to get the correct lists. aswell as printing student_list when done adding to it and print the prettified version'''
    for count,student in enumerate(student_list):
        add_to_student_list(calculate_weighted_grade(parts_list,student),count,student_list)
    print(student_list)
    grades_list = get_student_values(student_list)
    formated_list = get_formated_results(grades_list,parts_list)
    print(pretty_print(formated_list))

def main():
    '''Main function that get file objects and call corresponding functions'''
    filename_parts = input("Enter filename for parts: ")#'/home/star/HR/forritun/projects/course_grades/grade-parts.txt'
    file_parts_object = open_file(filename_parts)
    if file_parts_object == None:
        print(f"File {filename_parts} not found")
        return
    parts_list = parse_file_parts(file_parts_object)
    print(parts_list)
    filename_students = input("Enter filename for grades: ")#'/home/star/HR/forritun/projects/course_grades/grade-students.txt'
    file_student_object = open_file(filename_students)
    if file_student_object == None:
        print(f"File {filename_students} not found")
        return
    student_list = parse_file_students(file_student_object)
    print(student_list)
    calculate_and_print(parts_list,student_list)

main()