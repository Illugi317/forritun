'''Create a class called score with init,add,dec,str'''

class Score:
    def __init__(self,value:int=0) -> None:
        self.my_value = value
    
    def add(self,num):
        self.my_value += num
    
    def decrease(self,num):
        self.my_value -= num
    
    def __str__(self) -> str:
        return str(self.my_value)


if __name__ == '__main__':
    s = Score(4)
    print(s)
    s.add(20)
    print(s)
    s.decrease(10)
    print(s)