import string

def open_file(filename:str)-> object:
    ''' Open the file and return the file object, if it does not exist return None '''
    try:
        return open(filename,'r')
    except FileNotFoundError:
        return None

def get_word_list(file_object:object) -> list:
    ''' Get a list with per line as a nested list '''
    line_list = []
    for line in file_object:
        line_list.append(line.split())
    return line_list

def remove_punctuation_from_word(word:str) -> str:
    ''' Remove all punction from the specified word '''
    for punc in string.punctuation:
        if punc in word:
            word = word.replace(punc,"")
    return word

def join_list(parsed_word_list:list) -> list:
    ''' Join the nested lists together so we can split them later to create the keys '''
    joined_list = []
    for x in range(len(parsed_word_list)):
        joined_list.append(' '.join(parsed_word_list[x]))
    return joined_list

def parse_word_list(word_list:list) -> list:
    ''' Create the parsed list of words without punctiation and lowerd aswell a list that contains all the punctation and keeps the higher charaters for when we need to print the document '''
    print_list = [[]]
    doc_list = [[]]
    counter = 0
    for nested in word_list:
        if ''.join(nested) == "<NEWDOCUMENT>":
            print_list.append([])
            doc_list.append([])
            counter += 1
            continue
        print_str = ' '.join(nested)
        doc_str = ' '.join(nested) + " "
        doc_str = remove_punctuation_from_word(doc_str.lower())
        print_list[counter].append(print_str)
        doc_list[counter].append(doc_str)
    return doc_list,print_list

def create_key_list(word_list:list) -> list:
    ''' Create a list of all the words that occur in the file to use as the keys '''
    key_list = []
    for nested in word_list:
        for word in nested.split():
            key_list.append(word)
    return key_list

def create_dict(key_list:list) -> dict:
    ''' Create a dictionary from the key list with the default value of 0 '''
    word_dict = dict.fromkeys(key_list,set())
    return word_dict

def add_values(joined_list:list,key_list:list,word_dict:dict) -> dict:
    ''' Add the corresponding document values to the keys in the dict '''
    new_dict = {} 
    for key,value in word_dict.items():
        for idx,nested in enumerate(joined_list):
            if key + " " in nested: #If the word is in the sentence, the reason i add key + " " to prevent for example sales in salesman.
                try:
                    new_dict[key].add(idx) #Add the value to the dict
                except KeyError:
                    new_dic[key] = {idx} #If the key does not exist create the key and value in the dict
    return new_dict

def search_document(word_dict:dict,search_words:list,parse_word_list:list):
    ''' When the user wants to search when the correspoding words come up in the document, we need to find the sets of values from the dictionary
    and then we have to do an intersection across all the sets to find the corresponding values to print out. If the key or keys do not exist print out No match. '''
    try:
        results = [word_dict[key] for key in search_words] #Get corresponding sets
        results.sort() #sort the list
        current = results[0]
        for set_res in results[1:]:
            current &= set_res
        element_list = [x for x in current] #Since we cant use print(*set) to unpack the data we need to create a list of the integers
        element_list = sorted(element_list) #Sort the integers
        element_list_str = [str(a) for a in element_list] #Turn the integers to strings for printing
        print(f"Documents that fit search: {' '.join(element_list_str)} \n")
    except KeyError:
        print("No match.\n")

def print_document(print_list:list,doc_num:int):
    ''' Print the corresponding document which is a nested list of strings that is one line per string in the print list '''
    if doc_num >= len(print_list):
        print("No match.\n")
    else:
        print(f"Document #{doc_num}")
        for line in print_list[doc_num]:
            print(line)
    print("\n") #Mimir spec to get 2 newlines here

def print_menu():
    ''' The menu which the user can pick what to do '''
    print("What would you like to do?")
    print("1. Search Documents")
    print("2. Print Document")
    print("3. Quit Program")

def menu(set_dict:set,parse_word_list:list,print_doc_list:list):
    ''' TUI for the user, with error handling and calles the corresponding functions '''
    choice = "" #Menu start
    while choice != 3: 
        print_menu()
        try:
            choice = int(input("> "))
        except ValueError:
            choice = 3
        if choice == 1:
            search_words = input("Enter search words: ").lower().split()
            search_document(set_dict,search_words,parse_word_list)
        elif choice == 2:
            document_num = int(input("Enter document number: "))
            print_document(print_doc_list,document_num)
        elif choice == 3:
            print("Exiting program.")
            continue

def main():
    ''' The main function that calls all the functions and gets the data, aswell calls the menu for the user'''
    filename = '/home/star/HR/forritun/projects/document_retrival/ap_docs2.txt' #input("Document collection: ")
    file_object = open_file(filename)
    if file_object is None:
        print("Documents not found.")
        return
    line_list = get_word_list(file_object)
    parsed_word_list,print_doc_list = parse_word_list(line_list)
    joined_list = join_list(parsed_word_list)
    key_list = create_key_list(joined_list)
    word_dict = create_dict(key_list)
    set_dict = add_values(joined_list, key_list,word_dict)
    menu(set_dict,parsed_word_list, print_doc_list)

main()