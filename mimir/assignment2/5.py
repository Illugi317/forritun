'''
The theme park King’s Island needs to calculate its admission ticket prices.
When visitors come to the park and purchase tickets they might be eligible for a discount based on their age.

Each ticket cost $40. Senior citizens (age >= 65) are given a 40% discount.
People under 20 years of age get a 20% discount, and children under, or equal to, the age of 5 get a free admission.

Write a program that prompts for the visitor's age and computes and prints the ticket price (which should be a float).
'''

age = int(input("Input age: ")) # Do not change this line

if age >= 65:
    print(40 * 0.6)
elif 5 < age < 20:
    print(40 * 0.8)
elif age <= 5:
    print(0.0)
else:
    print(40.0)