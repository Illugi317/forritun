a0 = int(input("Input a positive int: "))   # Do not change this line

xn = a0
while True:
    if xn%2==0:
        xn = xn//2
    else:
        xn = xn * 3 + 1
    print(xn)
    if xn == 1:
        break