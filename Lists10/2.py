'''def getNumpeople():
    try:
        x = input("Number of people: ")
        c = int(x)
        return c
    except:
        print(f"{x} is not an integer. Please try again.")
        getNumpeople()

'''
def getAgeName(num_of_person):
    name = input(f"Name of person {num_of_person}: ")    
    try:
        age = input(f"Age of person {num_of_person}: ")
        int_age = int(age)
    except ValueError:
        print(f"{x} is not an integer. Please try again.")
        getAgeName(num_of_person)
    return [age,name]

def getMedian(nestedList):
    flatten = [val for sublist in nestedList for val in sublist]
    cleaned_flatten  = [x for x in flatten if x is not str]
    sortedl = sorted(cleaned_flatten)
    length = len(sortedl)
    index = (length - 1) // 2
    if (length % 2):
        return sortedl[index]
    else:
        return (sortedl[index] + sortedl[index + 1])/2.0

def avarage(nestedList):
    flatten = [val for sublist in nestedList for val in sublist]
    cleaned_flatten  = [int(x) for x in flatten if x.isnumeric()]
    sortedl = sorted(cleaned_flatten)
    return sum(sortedl)/len(sortedl)

def findOldestAndYoungest(nestedList):
    flatten = [val for sublist in nestedList for val in sublist]
    print(flatten)
    cleaned_flatten  = [int(x) for x in flatten if x.isnumeric()]
    print(cleaned_flatten)
    oldidx = cleaned_flatten.index(max(cleaned_flatten))
    youngestidx = cleaned_flatten.index(min(cleaned_flatten))
    return cleaned_flatten[oldidx],cleaned_flatten[oldidx+1],cleaned_flatten[youngestidx],cleaned_flatten[youngestidx+1]
    '''OldCounter = 0
    Oldidx = 0
    for idx,i in enumerate(flatten):
        if i >= Oldcounter:
            Oldcounter = i
            Oldidx = idx
    return flatten[idx], flatten[idx+1]
    '''
while True:
    x = input("Number of people: ")
    if x.isnumeric():
        number_of_people = int(x)
        break
    print(f"{x} is not an integer. Please try again.")   

nestedList = []
for i in range(1,number_of_people+1):
    nestedList.append(getAgeName(i))
    print(nestedList)
old_age, old_name, young_age, young_name = findOldestAndYoungest(nestedList)
print(f"The oldest person is {old_name} who is {old_age} years old")
print(f"The youngest person is {young_name} who is {young_age} years old")
print(f"The median age is {getMedian(nestedList)}")
print(f"The average age is {avarage(nestedList)}")

