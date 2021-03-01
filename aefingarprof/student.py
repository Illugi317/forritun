from collections import defaultdict
NUMBER_OF_PEOPLE = 4
NUMBER_OF_GRADES = 3
MAX_DECIMALS = 2
def get_names_and_values(name_dict):
    counter = 0
    while counter != NUMBER_OF_PEOPLE:
        name = input("Student name: ")
        for x in range(0,NUMBER_OF_GRADES):
            grade = input(f"Input grade number {x+1}: ")
            name_dict[name].append(float(grade))
        counter += 1

def show_student_list(name_dict):
    for key,value in name_dict.items():
        print(f"{key}: {value}")       

def get_highest_student(name_dict):
    print("Student with highest average grade:")
    highest_student = ""
    current_avg = 0
    for key,value in name_dict.items():
        avg = sum(value)/len(value)
        if current_avg < avg:
            current_avg = avg
            highest_student = key
    print(f"{highest_student} has an average grade of {round(current_avg,MAX_DECIMALS)}")

def main():
    name_dict = defaultdict(list)
    get_names_and_values(name_dict)
    show_student_list(name_dict)
    get_highest_student(name_dict)
main()