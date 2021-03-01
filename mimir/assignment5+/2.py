'''
The average (a.k.a. mean) and standard deviation are incredibly useful summary statistics.
The average tells us what the "central" value is for a set of data whereas the standard deviation tells us how close (or far)
away from the center the other values tend to be.

The average of n numbers is easy enough to calculate
a) sum up all the numbers
b) divide the sum by n.

Once the average has been calculated, the standard deviation is obtained by:
a) squaring the difference between each value and the average
b) summing up all those differences
c) dividing the sum by n
d) taking the square root

Notice how these steps resemble an algorithm.

...but this is too easy.

To make this more interesting, let's implement an algorithm that computes the running standard deviation.
A running standard deviation is calculated for every data point as it arrives.
This can be useful for very large data sets or when values are arriving in real-time (e.g. sensor measurements).

The program should repeatedly ask the user to type in an integer value and then print out the cumulative moving average and the standard deviation for each value that the user enters.
When printed, the summary statistics should be rounded to the 2nd decimal. Example:

        Enter a number (-1 to exit) 5
        Average: 5.0
        Standard deviation: 0.0
        Enter a number (-1 to exit) 3
        Average: 4.0
        Standard deviation: 1.0
        Enter a number (-1 to exit) 4
        Average: 4.0
        Standard deviation: 0.82
        Enter a number (-1 to exit) 7
        Average: 4.75
        Standard deviation: 1.48
        Enter a number (-1 to exit) -1

The WikiPedia article on standard deviation lays out how these calculations can be carried out,
albeit expressed using mathematical notation. We propose that you tackle this problem one step at a time:

1. Read the WikiPedia article and attempt to make sense of it.
    Think about how step-wise calculations, that compute the value at step k by using values from step k-1,
    could be implemented using a loop. If you are stranded, don't be afraid to ask a teacher or a fellow student for help.

2. Start by tackling the simpler problem: calculating the average. If you can solve that, then the rest becomes much easier.

3. Extend your solution to also update the standard deviation in every iteration of the loop.

NOTE: The program should calculate the population standard deviation, not the sample standard deviation.
'''

# You might need this to calculate a square root using math.sqrt
import math

# initialise-a tölurnar sem ég þarf að nota
number = 0
counter = 0

numbers = []

# Loop until the user types in -1
while number != -1:
    # Calculate the cumulative moving average and standard deviation
    number = int(input("Enter a number (-1 to exit) "))

    if number == -1:
        continue

    counter += 1

    numbers.append(number)

    current_average = sum(numbers) / counter

    differences = []
    for num in numbers:
        differences.append((num - current_average) ** 2)

    standard_deviation = math.sqrt(sum(differences) / counter)

    # Print them out within the loop
    print("Average:", round(current_average, 2))
    print("Standard deviation:", round(standard_deviation, 2))


# Proper Way to do it.

# You might need this to calculate a square root using math.sqrt
import math

current_sum = 0
current_sum_2 = 0
counter = 1

while True:
    input_value = int(input("Enter a number (-1 to exit) "))
    if input_value == -1:
        break

    # Calculate the cumulative moving average and standard deviation
    current_sum += input_value
    current_sum_2 += input_value ** 2
    current_average = current_sum / counter

    standard_deviation = math.sqrt((current_sum_2 / counter) - (current_average * current_average))

    # Print them out within the loop
    print("Average:", round(current_average, 2))
    print("Standard deviation:", round(standard_deviation, 2))

    counter += 1




