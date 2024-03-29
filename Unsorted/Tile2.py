def get_row(indexY, rows):
    return rows[indexY]


def check_lever(directions):
    return "L" in directions


def print_directions(directions):
    string = ""
    for direction in directions:
        if direction == "N":
            string += f"({direction})orth"

        elif direction == "S":
            string += f"({direction})outh"

        elif direction == "E":
            string += f"({direction})ast"

        elif direction == "W":
            string += f"({direction})est"
        if direction != "L":
            string += " or "

    # Til að taka út síðasta "or" og bæta við "."
    return string[:-4] + "."


def get_directions(indexX, row):
    return row[indexX]

def can_move_to_direction(indexX, row, direction):
    directions = get_directions(indexX, row)

    return direction in directions


def get_new_position_for_direction(direction, indexX, indexY):
    if direction == "N":
        return indexX, indexY + 1
    elif direction == "S":
        return indexX, indexY - 1
    elif direction == "W":
        return indexX - 1, indexY
    elif direction == "E":
        return indexX + 1, indexY

def play():
    coins = 0
    indexX = 0
    indexY = 0
    rows = [["ES", "EWL", "SW"],
        ["NESL", "SWL","NSL"],
        ["N", "N", "V"]]
    rows.reverse()

    valid = True
    while True:
        curr_row = get_row(indexY, rows)
        directions = get_directions(indexX, curr_row)
        if directions == "V":
            print(f"Victory! Total coins {coins}.")

            return input("Play again (y/n): ").lower() == "y"

        if check_lever(directions) and valid:
            choice = input("Pull a lever (y/n): ")

            if choice.lower() == "y":
                coins += 1
                print(f"You received 1 coin, your total is now {coins}.")


        print("You can travel:", print_directions(directions))

        direction = input("Direction: ")
        direction = direction.upper()

        if can_move_to_direction(indexX, curr_row, direction):
            indexX, indexY = get_new_position_for_direction(direction, indexX, indexY)
            valid = True
        else:
            print("Not a valid direction!")
            valid = False

def main():
    while play():
        pass

main()