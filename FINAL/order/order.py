class Order:
    def __init__(self,name:str,price:float):
        ''' Initilize the class with the values name and price as private class varibles'''
        self.__name = name
        self.__price = price
    
    def item(self):
        ''' Function to return the name of the item '''
        return self.__name
    
    def price(self):
        ''' Funtion to return the price of the item '''
        return self.__price

    def __str__(self):
        ''' String representation of the class object '''
        return f"Item: {self.__name}, price: {self.__price}"

    def __gt__(self,other):
        '''Overload the "greater than" operator, check if the self.__price is greater than the other.__price and if it is return True, otherwise return False '''
        if self.__price > other.__price:
            return True
        else:
            return False
    def __add__(self,other):
        ''' Add the order instances together, add the names to be "name1+name2" and add the prices together, and return a New Order object with the new name and new price'''
        new_name = self.__name + "+" + other.__name
        new_price = self.__price + other.__price
        return Order(new_name,new_price)


