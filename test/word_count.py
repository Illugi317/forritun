import os
import time
start_time = time.time()
punc = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
def open_file(filename):
    ''' Open the file and return the file object, if it does not exist return None '''
    try:
        return open(filename,'r')
    except FileNotFoundError:
        return None

def read_from_file_object(file:object):
    ''' Read from the file object and put it in a list and return it. '''
    all_file = []
    for line in file:
        all_file.append(line.split())
    return all_file
    
def main(filename):
    punc = ",.!?"
    punc_list = [str(a) for a in punc]
    file_object = open_file(filename)
    if file_object == None:
        print(f"File {filename} not found!")
        return
    all_file = read_from_file_object(file_object)
    new_list = []
    counter = 0
    for x in all_file:
        for i in x:
            counter += 1
            for k in i:
                if k in punc_list:
                    counter += 1
    print(counter)            


filename = "/home/star/HR/forritun/test/test1.txt"#input("Enter filename: ")
main(filename)
