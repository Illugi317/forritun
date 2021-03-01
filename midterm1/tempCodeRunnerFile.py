max_int = int(input("Input max integer:"))
empty_str = ""
for x in range(1,max_int+1):
    for i in range(1,x+1):
        print(i, end=" ")
    print()