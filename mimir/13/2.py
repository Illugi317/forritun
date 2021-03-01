


def get_word_list(file_obj) -> list:
    punc = ".,"
    word_list = []
    file_list = file_obj.readlines()
    for line in file_list:
        split_line = line.replace(',',' ').replace('.',' ').split()
        for x in split_line:
            word_list.append(x.lower())
    return word_list

def word_list_to_counts(word_list) -> dict:
    word_count = {}
    for word in sorted(word_list):
        word_count[word] = word_count.setdefault(word,0)+1
    return word_count

def dict_to_tuples(word_count_dict) -> list:
    new_list = []
    for key, value in word_count_dict.items():
        new_list.append((key,value))
    return new_list

def main():
    filename = input("Name of file: ")
    file_object = open(filename)
    word_list = get_word_list(file_object)
    file_object.close()
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuples(word_count_dict)
    print(sorted(word_count_tuples))
    
main()