'''
Write a program that, given a maxium number (max_num) from the user,
finds all positive integers n in the range 1 to max_num where n equals the cube of the sum of its digits.

The smallest two numbers which satisfy this property are 1 and 512 since

1**3 = 1

and

(5+1+2)**3 = 8**3 = 512
'''

max_num = int(input("Input maximum number: "))

for i in range(1, max_num + 1):
    summ = 0
    i_str = str(i)

    for j in i_str:
        summ += int(j)

    summ = summ ** 3

    if summ == i:
        print(i)
