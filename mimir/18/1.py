class Pair:
    def __init__(self,val1:int=0,val2:int = 0) -> None:
         self.__val1 = val1
         self.__val2 = val2

    def __repr__(self) -> str:
        return f"Value 1: {self.__val1}, Value 2: {self.__val2}"

    def __add__(self,other) -> "Pair":
        return Pair(self.__val1+other.__val1, self.__val2 + other.__val2)


pair1 = Pair(20,30)
print(pair1)
pair2 = Pair(40,50)
pair3 = pair1 + pair2
print(pair3)
