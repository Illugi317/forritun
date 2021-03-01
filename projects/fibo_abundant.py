choice = input("Input f|a|b (fibonacci, abundant or both): ")
if choice == 'f' or choice =='b':
    length = int(input("Input the length of the sequence: "))
    n1,n2 = 0,1
    print("Fibonacci Sequence:")
    print("-------------------")
    for x in range(length):
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
if choice == 'a' or choice == 'b':
        num = int(input("Input the max number to check: "))
        print("Abundant numbers:")
        print("-----------------")
        # Abundant numbers, ef við tökum 12 sem dæmi þá eru allar deilanlegar tölur 1,2,3,4,6 og summan af þvi er stærri en 12, hún er 16 og þá er talan 12 abundant number
        for i in range(1,num+1):
            summa = 0
            for j in range(1,i+1):
                if i%j==0 and j!=i:
                    summa += j
            if i < summa:
                print(i)
