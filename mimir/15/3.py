import string
from operator import itemgetter
def get_words(file_object):
    new_list = []
    for line in file_object:
        line_to_append = line.split()
        new_list += line_to_append
    return new_list

def remove_punc(word_list):
    for index,word in enumerate(word_list):
        word = word.lower()
        for punc in string.punctuation:
            if punc in word:
                word = word.replace(punc,"")
        word_list[index] = word

def get_dict(key_list:list) -> dict:
    bia_dict = dict.fromkeys(key_list,0)
    return bia_dict

def values_into_dict(key_list,bia_dict):
    for key in key_list:
        if key in bia_dict.keys():
            bia_dict[key] += 1
    return bia_dict

def create_key_list(word_list:list):
    key_list = []
    try:
        for word in range(len(word_list)):
            key_list.append((word_list[word],word_list[word+1]))
    except IndexError:
        pass
    return key_list

        
def main():
    filename = input("Enter name of file: ")
    file_object = open(filename)
    word_list = get_words(file_object)
    file_object.close()
    remove_punc(word_list)
    key_list = create_key_list(word_list)
    my_dict = get_dict(key_list)
    bia_dict = values_into_dict(key_list,my_dict)
    change_to_list = list(bia_dict.items())
    sorted_list = sorted(change_to_list,key=itemgetter(0))
    sorted_list = sorted(sorted_list,key=itemgetter(1),reverse=True)
    print(sorted_list[:10])

main()