def rotate_text_clockwise(text):
    """ Rotates text 90 degrees clockwise, adding spaces as needed for multi-line strings """
    # ... add your implementation

    max_line_length = 0

    for lines in text.splitlines():
        max_line_length = max(max_line_length, len(text.splitlines()))

    new_str = ""

    for i in range(max_line_length):
        lines = text.splitlines()
        lines.reverse()
        for line in lines:
            if len(line) <= i:
                continue
            new_str += line[i]
        new_str += "\n"

    return new_str.strip()

string = """,g
rn
eo
tr?
nwu
i o
rsy
p' 
 th
yat
ehi
Hww"""

print(rotate_text_clockwise(string))