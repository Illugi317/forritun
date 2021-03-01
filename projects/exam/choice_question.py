from question import Question
class ChoiceQuestion(Question):
    """
    Class to hold on to the mulitiple choice question

    Functions 
    -------
    __init__()
        Create a list to hold on to the choices to the question
        Aswell as use the super function to inherit the parent class

    add_choice(choice:str,correct:bool)
        Adds a choice to the list of choices for the question, if the boolean value of correct is True it aslo sets the answer to that element in the list (The number of the element )
        
    __str__()
        Returns a string of all the choices numberd with a newline in between them. uses Rstrip to remove the trailing newline
    """
    def __init__(self):
        self.__choicelist = []
        super().__init__()

    def add_choice(self,choice:str,correct:bool):
        self.__choicelist.append((choice,correct))
        if correct == True:
            self.set_answer(len(self.__choicelist))

    def __str__(self):
        choices_print_str = f"{self._Question__question}\n"
        for idx,choices in enumerate(self.__choicelist):
            choices_print_str += f"{idx+1}. {choices[0]}\n"
        return choices_print_str.rstrip()
