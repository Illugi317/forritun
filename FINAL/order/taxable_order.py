from order import Order
class TaxableOrder(Order):
    def __init__(self,name:str,price:float,taxable:float):
        ''' Inherit the init function of the Order class and calculate the price accordingly '''
        Order.__init__(self,name,round(price + (price*taxable),2))
