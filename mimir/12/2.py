'''
Write two functions for removing even numbers from integer lists:

    remove_evens(int_list): Removes even integers from int_list, thus modifying int_list
    remove_evens2(int_list): Returns a new list with only odd integers from int_list, without modifying int_list

Example main program and input/output:

a_list = [1,2,2,3,4,5]
print(a_list)
remove_evens(a_list)
print(a_list)
    
b_list = [1,2,3,4,4,5,6,7,8,9,10]
c_list = remove_evens2(b_list)
print(b_list)
print(c_list)

[1, 2, 2, 3, 4, 5]
[1, 3, 5]
[1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
[1, 3, 5, 7, 9]

Hint: Functions have the ability to modify mutable objects in the calling program. Lists are mutable objects. 
'''
def remove_evens(a_list):
    for index in range(len(a_list)-1,-1,-1):
        if a_list[index] % 2 == 0:
            a_list.pop(index)
def remove_evens2(some_list):
    new_list = []
    for x in some_list:
        if x%2==1:
            new_list.append(x)
    return new_list


# Main starts here
a_list = [1,2,2,3,4,5]
print(a_list)
remove_evens(a_list)
print(a_list)
    
b_list = [1,2,3,4,4,5,6,7,8,9,10]
c_list = remove_evens2(b_list)
print(b_list)
print(c_list)