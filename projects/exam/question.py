class Question:
    """
    Class to hold on to a Question

    Functions
    -------
    set_question(question:str)
        Stores the question string in a private class variable called self.__questions 

    set_answer(answer:str)
        Store the answer in a private class variable called self.__answer

    check_answer(guess:str)
        Check if the guess matches the answer given

    __str__()
        Returns the question string

    __repr__()
        Returns a formatted version of the question and answer string
    """
    def set_question(self,question:str):
        ''' Set the questions string '''
        self.__question = question

    def set_answer(self,answer:str):
        ''' Set the answer string '''
        self.__answer = answer

    def check_answer(self, check:str):
        self.__check = check
        if str(self.__check).lower() == str(self.__answer).lower():
            return True
        else:
            return False
    def __str__(self):
        return f"{self.__question}"

    def __repr__(self):
        return f"Q: {self.__question} A: {self.__answer}"


