dog_age = int(input("Input dog's age: ")) # Do not change this line
human_age = 0
if dog_age <= 0 or dog_age > 16:
    print("Invalid age")
elif dog_age == 1:           #Tvær if setningar til að prenta út 15 og 24 því restin er síðan +4
    print("Human age:",15)
elif dog_age == 2:
    print("Human age:",24)
else:
    human_age += 24
    for x in range(1,dog_age - 1):
        human_age += 4
    print("Human age: ",human_age)
    