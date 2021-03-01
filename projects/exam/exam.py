from question import Question
from choice_question import ChoiceQuestion
class Exam:
    """
    Class for the Exam

    Föll
    -------
    __init__()
        Creates .__score and .__question_list
        .__score keeps the current score
        .__question_list keeps the questions in order they were createad

    add_question(question_str:str,answer_str:str)
        Adds a question to the Exam.

    add_choice_question(question_str:str, choice_list:list)
        Adds a multiple choice question

    get_points()
        Returns the current points
    
    get_num_questions()
        Returns the amound of questions

    present_exam()
        Starts the exam and asks the user for the answers to the questions
    """
    def __init__(self):
        self.__score = 0
        self.__question_list = []

    def add_question(self,question_str:str,answer_str:str):
        ''' Bætir við spurningu með því að kalla á klassan Question og bætir við spurninguni og svarinu og að lokum er set það í spurninga listann '''
        question_object = Question()
        question_object.set_question(question_str)
        question_object.set_answer(answer_str)
        self.__question_list.append(question_object)

    def add_choice_question(self,question_str:str, choices_list:list):
        ''' Bætir við krossaspurningu með því að kalla á klassan ChoiceQuetion og bætir við spurninguni og svöronum við klassa objectið og að lokum er það bætt við í spurninga listann '''
        choice_object = ChoiceQuestion()
        choice_object.set_question(question_str)
        for choice in choices_list:
            choice_object.add_choice(choice[0],choice[1])
        self.__question_list.append(choice_object)

    def get_points(self):
        return self.__score

    def get_num_questions(self):
        return len(self.__question_list)

    def present_exam(self):
        ''' Prints a question from the question_list and requests a answer from the user. if the answer is correct, increment self.__score by 1'''
        for question in self.__question_list:
            print(question)
            response = input("Your answer: ")
            print(f"{question.check_answer(response)}\n")
            if question.check_answer(response):
                self.__score += 1
