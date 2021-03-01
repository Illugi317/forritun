import math

start_int = int(input("Input starting integer: "))
number1 = start_int
number2 = 0 
for x in range(start_int):
    if number1 < 2: #Ef tala er minni en 1.4 break
        break
    number1 = math.sqrt(number1) # Taka rót, síðan taka rót af rót
    print(round(number1,4)) #Prenta rót með 4 aukastöfum
