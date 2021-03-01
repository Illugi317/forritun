'''
Those pesky Romans are about to attack your village.
Luckily your spies have managed to intercept letters from their general and you hope that one of them contains information about the timing of the attack.
There's only one problem; they are encrypted!

The Romans use an encryption system which is based on shifting the letters of the alphabet.
For example,
the word ATTACK becomes CVVCEM when the letters are shifted by 2 (A -> C, T -> V, K -> M). In order to decrypt those message,
you just have to find out by how many letters you must shift each character.

As you look at the encrypted messages,
you notice a pattern. The first line is always the same length. Hmm,
could this be a greeting of some sorts, you ask yourself.

Kdlo/#Fdhvdu$

Using an ASCII table and pen and paper, you try different shifts until you finally crack it. The first line says:

Hail, Caesar!

This is brilliant! Now you can figure out which shift was used just by looking at the first character!

Since you have a large number of messages to decrypt, each of which may have been encrypted with a different shift,
you decide to write a program to do so. But hurry, the fate of your village may depend on your programming skills.
Input and Output

Every message is exactly 4 lines. Given the following input:

    Jckn."Ecguct#
    Dg"tgcf{"hqt"cvvcem
    Fqp)v"ngv"vjg"gpgo{"ugg"{qw
    Ocmg"uwtg"Dtwvwu"uvc{u"swkgv

the program should print out the decrypted message, which in this case is:

    Hail, Caesar!
    Be ready for attack
    Don't let the enemy see you
    Make sure Brutus stays quiet

Hints

Python has two built-in methods, ord()and chr(), which convert letters to numbers and vice versa.

All encrypted strings and all decrypted strings should consist of letters belonging the set of "printable characters" in the ASCII table,
i.e. characters numbered from 32 to 126 inclusive.
Take care to wrap numbers around should they be shifted outside of this range.

Python strings are iterable.
'''


'''
# Read exactly four lines of input
line1 = "Mfnq1%Hfjxfw&"
line2 = "Mt|%nx%ymj%|jfymjwD"
line3 = "Ny,x%{jw~%mty%t{jw%mjwj3"
line4 = "ux3%Gwzyzx%ktwlty%mnx%xfsifqx3"
'''
# Read exactly four lines of input
line1 = input()
line2 = input()
line3 = input()
line4 = input()

# Define variables for the range of numbers within which we have 'printable' characters.
# As we shift the input characters, we must ensure that they stay within this range.
LOW = ord(" ")  # 32
HIGH = ord("~")  # 126

# Every transmission starts with the line "Hail Caesar!" so the first letter,
# once decrypted, must be H.
first_letter = line1[0]
# ...now find out what the key is

h_num = ord("H")
num = ord(first_letter)

shifted = num - h_num

# We can use 'for' to iterate over the lines and decrypt them one by one
for line in (line1, line2, line3, line4):
    # ... and the rest is up to you
    for letter in line:
        ord_num = ord(letter)

        new_ord_num = ord_num - shifted

        if new_ord_num < 32:
            # 32 = ord_num - x
            x = ord_num - 32

            new_shifted = shifted - x

            new_ord_num = 127 - shifted

        elif new_ord_num > 126:
            # 126 = ord_num - x
            x = ord_num - 126

            new_shifted = shifted - x

            new_ord_num = 31 - shifted

        new_letter = chr(new_ord_num)
        print(new_letter, end="")

    print()