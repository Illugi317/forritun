'''
*This is a challenging exercise!

Write a Python program that calculates the sum of any number of vectors (all of which have the same dimension).

The sum of vectors v1, v2, ..., vn is defined as a single vector whose elements are the sum of the corresponding elements in v1, v2, ..., vn

For example (for n=3):

[1, 3, -5] + [4, -2, 1] + [2, 5, 3] = [7, 6, -1]

The values for each element of the vectors are read from a file.

The file, vectors.txt, for the above vectors looks like this:

1 3 -5
4 -2 1
2 5 3

Example input/output:

Enter filename: vectors.txt
[[1, 3, -5], [4, -2, 1], [2, 5, 3]]
[7, 6, -1]

As can be seen, once the data has been read from the input file, the vectors (a list of lists) is printed, before the result is printed.
'''
def read_numbers_from_file(filename):
    numbers = []

    with open(filename, "r") as file:
        for line in file:
            numbers.append([int(x) for x in line.split()])

    return numbers

def sum_of_vectors(vectors, length):
    vector_sum = [0] * length

    for vector in vectors:
        for i in range(length):
            vector_sum[i] += vector[i]

    return vector_sum

filename = input("Enter filename: ")
numbers = read_numbers_from_file(filename)
print(numbers)
print(sum_of_vectors(numbers, len(numbers[0])))