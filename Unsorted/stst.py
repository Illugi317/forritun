length = int(input(">> "))

num = 0

counter = 0

while True:
    num = str(num)
    num = num.zfill(length)
    if "11" in num:
        counter += 1
    elif "22" in num:
        counter += 1
    elif "33" in num:
        counter += 1
    elif "44" in num:
        counter += 1
    elif "55" in num:
        counter += 1
    elif "66" in num:
        counter += 1
    elif "77" in num:
        counter += 1
    elif "88" in num:
        counter += 1
    elif "99" in num:
        counter += 1
    elif "00" in num:
        counter += 1

    num = int(num) + 1

    if len(str(num)) > length:
        break

print(counter)