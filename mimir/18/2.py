class MyString():
    def __init__(self,string:str=""):
        self.string = string
    def __repr__(self):
        return f"{self.string}"
    def __gt__(self,other):
        return len(self.string) > len(other.string)
    def __sub__(self, other):
        return abs(len(self.string) - len(other.string))
        


str1 = MyString('This is a string')
str2 = MyString('This is another one')
print(str1 > str2)
print(str1 - str2)