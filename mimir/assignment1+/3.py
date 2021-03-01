'''
Your kitten, Zero, has contracted the sniffles.
Zero is a very sociable kitten so you suspect that it may have spread the disease.
You wonder how many kittens are likely to become ill.
You check on Wikipedia and see that the common cold has a basic reproduction number (R0) between 2 and 3.
You grab a napkin and do the math. Suppose that R0 is 2. Then Kitten Zero infects two kittens,
who each then infect two other kittens and so on and so forth. After 3 rounds of transmissions the total number of cases is:
1 + 2 + (2*2) + (2*2*2) = 15

But what if R0 is 2.5...or 2.7...or 2.67?
That's a bit harder to calculate by hand so you write a program to compute the answer, rounded to the nearest kitten.
'''

r_0 = float(input("What's the basic reproduction rate (R_0)? "))
# Convert input to float
# Calculate the expected number of cases after 3 rounds of transmission originating
total_cases = round(1 + r_0 + (r_0*r_0) + (r_0*r_0*r_0))

# from kitten Zero
print("Total cases after 3 rounds of transmission:", round(total_cases))