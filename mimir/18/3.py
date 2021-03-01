class Rectangle:
    def __init__(self,length: int = 1, width:int = 1):
        self.__length = max(length,1)
        self.__width = max(width,1)
    def area(self):
        return self.__length * self.__width
    def perimeter(self):
        return self.__length*2 + self.__width*2

    def __str__(self):
        return f"Length: {self.__length}, Width: {self.__width}"

    def __repr__(self):
        return f"Rectangle({self.__length},{self.__width})"

    def __eq__(self,other):
        return self.area() == other.area()