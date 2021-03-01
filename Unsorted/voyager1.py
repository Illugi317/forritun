a = int(input("Number of days after 9/25/09: "))
dist = 16637000000
constantspeed = 38241
days = constantspeed * 24
total = (days * a) + dist
km = total * 1.609344
print("Miles from the sun:", total)
print("Kilometers from the sun:", round(km))
print("AU from the sun:",round(total / 92955887.6))