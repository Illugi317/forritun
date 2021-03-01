def make_new_row(row):
    new_row = []
    if row==[]:
        return[1]
    row_index = 0

    for i in range(len(row)+1):
        if i == 0 or i==len(row):
            new_row.append(1)
            continue
        
        new_row.append(row[row_index]+ row[row_index+1])
        row_index += 1
    return new_row

height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)
