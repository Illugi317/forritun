class NaturalNumber:
    def __init__(self,num:int=0):
        if not isinstance(num,int) or num < 0 :
            self.__num = None
        else:
            self.__num = num
    def __str__(self):
        return f"{self.__num}"
    def __add__(self, other):
        if self.__num is None or other.__num is None:
            return None
        else:
            return NaturalNumber(self.__num + other.__num)
    def __mul__(self,other):
        if self.__num is None or other.__num is None:
            return None
        else: 
            return NaturalNumber(self.__num * other.__num)
    def __sub__(self,other):
        if self.__num is None or other.__num is None:
            return None
        else:
            return NaturalNumber(self.__num - other.__num)


num1 = NaturalNumber("bla")

print(num1)