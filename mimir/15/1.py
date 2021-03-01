def list_attempt(first:str, last:str) -> list:
    list_of_letters = []
    for first_char in first:
        for last_char in last:
            if first_char == last_char:
                if first_char not in list_of_letters:
                    list_of_letters.append(first_char)

    return list_of_letters

def set_attempt(first:str, last:str) -> set:
    set_of_letters = set()
    for first_char in first:
        for last_char in last:
            if first_char == last_char:
                set_of_letters.add(first_char)

    return set_of_letters

def sorted_list(a_list):
    return sorted(a_list)

def main():
    name = input("Enter name: ").split()
    first = name[0].lower()
    last = name[1].lower()
    list_of_letters = list_attempt(first, last)
    set_of_letters = set_attempt(first, last)
    print(sorted_list(list_of_letters))
    print(sorted_list(set_of_letters))

main()