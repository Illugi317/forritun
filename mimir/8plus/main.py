# ...add your functions
def open_file(filename:str):
  try:
    return open(filename,"r")
  except:
    return None

def how_many_lines(writeobj:object):
    for i,line in enumerate(writeobj):
        pass

    writeobj.seek(0)
    return i+1

# You can keep these lines
file_name_a = input("First file: ")
file_name_b = input("Second file: ")

# ...fill in the rest
fileobj_a = open_file(file_name_a)
fileobj_b = open_file(file_name_b)

counterA = how_many_lines(fileobj_a)
counterB = how_many_lines(fileobj_b)
counter = max(counterA,counterB)
for x in range(counter):
    print(fileobj_a.readline())
    print(fileobj_b.readline())