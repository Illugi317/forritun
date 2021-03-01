n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
prime = False
counter = 0
x = 2
while ( x <= n//2 ):
    if(n % x == 0):
        counter = counter + 1
        break
    x = x + 1
if counter == 0 and n != 1:
    prime = True
# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")