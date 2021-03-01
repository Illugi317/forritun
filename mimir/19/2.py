class Student:
    def __init__(self,id_num:int,grades:list) -> None:
        self.__id = id_num
        self.__grades = grades
    def get_avg(self):
        summa = [x for x in self.__grades]
        avg = len(self.__grades) / sum(summa)
        return avg
    def __lt__(self,other):
        if other.get_avg() < self.get_avg():
            return True
        else:
            return False
    def __str__(self):
        return f"Student ID: {self.__id}\nGrades: {self.__grades}"

'''
Implement the class Student.  An instance of the class has variables for student id (integer) and a list of four float grades. An instance is created like: 

student1 = Student(1, [3.0, 4.6, 3.4, 5.4])

When an instance of a student is printed,  the result should be as follows:

Student ID: 1
Grades: [3.0, 4.6, 3.4, 5.4]


It should be possible to compare two students with the < operator.  The comparison is based on the average grade of the instances:

student1 = Student(1, [3.0, 4.6, 3.4, 5.4])
student2 = Student(2, [9.5, 9.0, 8.9, 9.8])

if student1 < student2:
    print("student1 < student2")

You should only hand in the code for the class, not any main program.


'''