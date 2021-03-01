max_int = int(input("Input max integer: "))
for x in range(1,max_int+1): 
    for i in range(1,x+1):
        print(i, end=" ") #Nota end = " " til að halda áfram að prenta á sömu línu
    print()