number_to_multiply = int(input("Input number to multiply: ")) # Do not change this line
how_often = int(input("Input how often to multiply: ")) # Do not change this line
summa = 0
for x in range(how_often):
    summa += number_to_multiply
    print(summa)
