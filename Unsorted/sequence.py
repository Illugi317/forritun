n = int(input("Enter the length of the sequence: ")) # Do not change this line
a = 1
b = 2
c = 3
for x in range(n):
    print(a)
    ctemp = c #taka þessa til hliðar
    btemp = b #lika þessa
    c = a + b + c #reikna næstu c tölu
    b = ctemp 
    a = btemp


