# The Python program calculates circle areas and circumreference for entered
# radiuses and a sum of all circle areas/circumreferences.

import math

print("The Python program calculates circle areas for entered radiuses and a sum of all circle areas")
print()

n = int(input("Enter number of circles: "))

# A list that stores all entered radiuses. Its empty at start.
radiuses = []

# Input all radiuses
print("Enter radiuses ...")
for i in range(n):
    r = float(input(f"r[{i+1}]: "))
    radiuses.append(r)

# Print a table of entered data and calculated values
print()
print(f"{'i':>5} {'radius':>10} {'area':>10} {'cref':>10}")
print("-" * 43)
for i in range(n):
    a = math.pi * radiuses[i]**2
    c = 2 * math.pi * radiuses[i]
    print(f"{i + 1:5} {radiuses[i]:10.2f} {a:10.2f} {c:10.2f}")

# Calculate sum area/circumreference of all circle
print()
a_sum = 0
c_sum = 0
for i in range(n):
    a_sum = a_sum + math.pi * radiuses[i]**2
    c_sum = c_sum + 2 * math.pi * radiuses[i]

print(f"Total area of circles: {a_sum:.2f}")
print(f"Total circumreference of circles: {c_sum:.2f}")
print()
print("End.")
