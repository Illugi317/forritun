 # Read exactly four lines of input
line1 = input()
line2 = input()
line3 = input()
line4 = input()

# Define variables for the range of numbers within which we have 'printable' characters.
# As we shift the input characters, we must ensure that they stay within this range.
LOW = ord(" ")  # 32
HIGH = ord("~") # 126

# Every transmission starts with the line "Hail Caesar!" so the first letter, 
# once decrypted, must be H.
first_letter = line[0]
# ...now find out what the key is
h_num = ord('H')
tnum = ord(first_letter)
shifted = tnum - h_num
# We can use 'for' to iterate over the lines and decrypt them one by one
for line in (line1, line2, line3, line4):
    # ... and the rest is up to you# Read exactly four lines of input
    for letter in line:
        num = ord(letter)
        newnum = num - shifted
        if newnum < 32:
            x = num - 32
            ns = shifted - x
            newnum = 127 - shifted
        elif newnum > 126:
            x = num - 126
            ns = shifted - x
            newnum = 31 - shifted
        nletter = chr(newnum)
        print(nletter, end='')
    print()
