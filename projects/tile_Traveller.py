row1 = "ES/EW/WS/"
row2 = "NES/WS/NS/"
row3 = "N/N/V/"

indexY = 0
indexX = 0

def position(indexX,row):
    counter = -1
    idx = 0
    last = 0
    for i in row:
        if i == "/":
            counter += 1
            if counter == indexX:
                return row[last:idx]
            else:
                last = idx
        idx += 1

def canMove(indexX,row,direction):
    s = position(indexX,row)
    if direction in s:
        return True
    else:
        return False
def changeIdx(direction,indexY,indexX):
    if direction == "N":
        indexY += 1
        return indexY,indexX
    elif direction == "E":
        indexX += 1
        return indexY,indexX
    elif direction == "S":
        indexY -= 1
        return indexY,indexX
    elif direction == "W":
        indexX -= 1
        return indexY,indexX

def getRow(indexY,row1,row2,row3):
    if indexY == 0:
        return row3
    elif indexY == 1:
        return row2
    elif indexY == 2:
        return row1

def printDirections(row):
    string = ""
    for x in row:
        if x == "N":
            string += "(N)orth or "
        elif x == "E":
            string += "(E)ast or "
        elif x == "S":
            string += "(S)outh or "
        elif x == "W":
            string += "(W)est or "
    string = string[:-4] + "."
    return string
while True:
    where_can_go = printDirections(position(indexX,getRow(indexY,row1,row2,row3)))
    if position(indexX,getRow(indexY,row1,row2,row3)) == "/V":
        print("Victory!")
        break
    current = getRow(indexY,row1,row2,row3)
    print(f"You can travel: {where_can_go}")
    direction = input("Direction: ")
    direction = direction.upper()
    if canMove(indexX,current,direction):
        indexY, indexX=changeIdx(direction,indexY,indexX)
    else:
        print("Not a valid direction!")






