def find_index_of_nth_occurrence(sequence, element_to_find, occurrence):
    """ Returns the location of the n-th occurrence of an element within a sequence """
    # ... and the rest is up to you 
    counter = 0
    index = 0
    for char in sequence:         
        if char == element_to_find:
            counter += 1
            if counter == occurrence:                                                                                    
                return index
        index += 1    
    else:
        return -1

def remove_at(sequence, index_to_remove):
    """ Removes an element from a sequence at the specified index. 
    
    Returns the updated sequence and the element that was removed, in that order.
    """
    # ... and the rest is up to you
    char = sequence[index_to_remove]
    sequence = sequence[:index_to_remove] + sequence[index_to_remove+1:]
    return sequence,char

def insert_at(sequence, index, element):   
    """ Inserts an element at the specified location in a sequence and returns the updated sequence. """
    sequence = sequence[:index] + element + sequence[index:]              
    return sequence     

def move_one(from_pillar, to_pillar, state):
    """ Moves the topmost disc from one pillar to another and returns the updated state representation. """
    # ... implement this method, utilizing the functions defined above
    
    pillar_form_end = find_index_of_nth_occurrence(state, "|", from_pillar)
    state, char = remove_at(state, pillar_form_end - 1)
    pillar_to_end = find_index_of_nth_occurrence(state, "|", to_pillar)
    
    return insert_at(state, pillar_to_end, char)
# ... add your functions from the previous solution here at the top

def move_many(how_many, from_pillar, to_pillar, state):
    """ Moves the specified number of discs from one pillar to another and returns the updated state representation. 
    
    Prints the state for every move made.
    """
    # ... implement this method
    if how_many == 0:
        return state

    remaining_pillar = 0
    if from_pillar != 1 and to_pillar != 1:
        remaining_pillar = 1
    elif from_pillar != 2 and to_pillar !=2:
        remaining_pillar = 2
    elif from_pillar !=3 and to_pillar !=3:
        remaining_pillar = 3
    #state = move_many(how_many-1,from_pillar,remaining_pillar,state)
    state = move_many(how_many-1,from_pillar,remaining_pillar,state)
    state = move_one(from_pillar,to_pillar,state)
    print(state)
    return move_many(how_many-1,remaining_pillar,to_pillar,state)

# Keep the following lines as they are
number_of_discs = int(input("How many discs are on the left-most pillar? "))
initial_state = ""
for disc in range(number_of_discs, 0, -1):
    initial_state += str(disc)
initial_state += "|||"
print(initial_state)
move_many(how_many=number_of_discs, from_pillar=1, to_pillar=3, state=initial_state)
