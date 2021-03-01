class Portfolio:
    def __init__(self)-> None:
        self.stocks = []

    def add(self,stock):
        self.stocks.append(stock)

    def __str__(self) -> str:
        string = ""
        for stock in self.stocks:
            string += stock.__str__()
            string += '\n'
        return string.strip()

class Stock:
    def __init__(self,name,shares:int=0) -> None:
        self.name = name
        self.shares = shares
    def __str__(self) -> str:
        return f"{self.name}: {self.shares}"

if __name__ == '__main__':
    stock1 = Stock('IBM', 100)
    print(stock1)
    stock2 = Stock('GOOG', 200)
    stock3 = Stock('AMZN', 500)

    folio = Portfolio()
    folio.add(stock1)
    folio.add(stock2)
    folio.add(stock3)
    print()

    print(folio)

    print(Portfolio())