digit = 10
while True:
    summ = pow(digit,2)
    if digit == int(str(summ)[1:]):
        print(digit)
    digit += 1
    if digit == 100:
        break