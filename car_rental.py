print("Welcome to car rentals!")
while True:
    if input("Would you like to continue (y/n)? ") != "y":
        break
    #skilgreina breytur
    customercode = input("Customer code (b or d): ") 
    days = int(input("Number of days: "))
    odostart = int(input("Odometer reading at the start: "))
    odoend = int(input("Odometer reading at the end: "))
    milesdriven = odoend - odostart
    print("Miles driven: ",milesdriven)
    #if setningar til að skilgreina milli customercode
    if customercode == "b":
        moneydue = (40 * days)+(milesdriven * 0.25)
        print("Amount due:",round(moneydue,1))
    if customercode == "d":
        milesover = (milesdriven - (days * 100))
        moneydue = (60 * days)+(milesover * 0.25)
        print("Amount due:",round(moneydue,1))
