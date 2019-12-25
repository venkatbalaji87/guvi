import math

# Take input from user
base = int(input("Enter base : "))
exponent = int(input("Enter exponent : "))

power = 1

for i in range(1, exponent + 1):
    power = power * base

print("\nResult", base, "^", exponent, ":", power)

