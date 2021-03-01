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

