# You might need this to calculate a square root using math.sqrt
import math

summa = 0
summa2 = 0
count = 0
# Loop until the user types in -1
while True:
    count += 1
    num = int(input("Enter a number (-1 to exit) "))
    if num == -1:
        break
    # Calculate the cumulative moving average and standard deviation
    summa += num
    summa2 += num ** 2
    avg_summa = summa / count
    current_avarage = avg_summa
    # Print them out within the loop
    standard_deviation = math.sqrt((summa2 / count)-(avg_summa * avg_summa))
    print("Average:", round(current_avarage, 2))
    print("Standard deviation:", round(standard_deviation, 2))
