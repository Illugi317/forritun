class CashRegister:
    def __init__(self,tax_rate):
        self.__tax_rate = tax_rate/100
        self.__items = []

    def add_item(self,price,is_taxable):
        self.__items.append((price,is_taxable))

    def get_count(self):
        return len(self.__items)
    
    def clear(self):
        self.__items = []

    def get_total(self):
        return sum([x[0] for x in self.__items])

    def get_total_with_tax(self):
        is_taxable = []
        is_not_taxable = []
        summa = 0
        for x in self.__items:
            if x[1] == True:
                is_taxable.append(x[0])
            else:
                is_not_taxable.append(x[0])
        
        for price in is_taxable:
            tax = price * self.__tax_rate
            summa += price + tax
        return round(summa + sum(is_not_taxable),4)

    def __str__(self):
        return f"Items: {self.get_count()}, total price: {self.get_total():.2f}, including tax: {self.get_total_with_tax():.2f}"

        


reg1 = CashRegister(7.5)

reg1.add_item(10.0, True)

reg1.add_item(15.5, True)

reg1.add_item(23.3, False)

assert reg1.get_count() == 3

assert reg1.get_total() == 48.8

assert reg1.get_total_with_tax() == 50.7125

assert str(reg1) == 'Items: 3, total price: 48.80, including tax: 50.71'

reg1.clear()

assert str(reg1) == 'Items: 0, total price: 0.00, including tax: 0.00'
