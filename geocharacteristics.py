# Functions for calculating geometric characteristics

def Ax(n, x, y):
    v = 0.0
    for i in range(n):
        v = v + (x[i+1] + x[i]) * (y[i+1] - y[i])

    return 0.5 * v

def Sx(n, x, y):
    v = 0.0
    for i in range(n):
        v = v + (x[i+1] - x[i]) * (y[i+1]**2 + y[i] * y[i+1] + y[i]**2)

    return -1. / 6. * v

def Sy(n, x, y):
    v = 0.0
    for i in range(n):
        v = v + (y[i+1] - y[i]) * (x[i+1]**2 + x[i] * x[i+1] + x[i]**2)

    return 1. / 6. * v

def Ix(n, x, y):
    v = 0.0
    for i in range(n):
        v = v + (x[i+1] - x[i]) * (y[i+1]**3 +  y[i+1]**2 * y[i] + y[i+1] * y[i]**2 + y[i]**3)

    return -1. / 12. * v

def Iy(n, x, y):
    v = 0.0
    for i in range(n):
        v = v + (y[i+1] - y[i]) * (x[i+1]**3 +  x[i+1]**2 * x[i] + x[i+1] * x[i]**2 + x[i]**3)

    return 1. / 12. * v

def Ixy(n, x, y):
    v = 0.0
    for i in range(n):
        v = v + (y[i+1] - y[i]) * (y[i+1] * (3* x[i+1]**2 + 2 * x[i] * x[i+1] + x[i]**2) + y[i] * (3 * x[i]**2 + 2 * x[i] * x[i+1] + x[i+1]**2))

    return -1. / 24. * v

def xt(n, x, y):
    return Sy(n, x, y) / Ax(n, x, y)

def yt(n, x, y):
    return Sx(n, x, y) / Ax(n, x, y)

def Ixt(n, x, y):
    return Ix(n, x, y) - yt(n, x, y)**2 * Ax(n, x, y)

def Iyt(n, x, y):
    return Iy(n, x, y) - xt(n, x, y)**2 * Ax(n, x, y)

def Ixyt(n, x, y):
    return Ixy(n, x, y) + xt(n, x, y) * yt(n, x, y) * Ax(n, x, y)


# Data input

n = int(input("Enter the number of polygon points: "))

x = []
y = []

print()
print("Enter x and y coordinates for polygon points ...")
for i in range(n):
    line = input(f"Point {i + 1}: ")
    words = line.split()

    x.append(float(words[0]))
    y.append(float(words[1]))

x.append(x[0])
y.append(y[0])

# Print table to screen

print()
print(f"{'Point':10} {'x':10} {'y':10}")
print("-" * 30)
for i in range(n):
    print(f"{i+1:<10d} {x[i]:<10.2f} {y[i]:<10.2f}")

# Print results to screen

print()
print("Geometric characteristics:")
print(f"{'Ax':6} {Ax(n, x, y):5.2f}")
print(f"{'Sx: ':6} {Sx(n, x, y):5.2f}")
print(f"{'Sy: ':6} {Sy(n, x, y):5.2f}")
print(f"{'Ix: ':6} {Ix(n, x, y):5.2f}")
print(f"{'Iy: ':6} {Iy(n, x, y):5.2f}")
print(f"{'Ixy: ':6} {Ixy(n, x, y):5.2f}")
print(f"{'xt: ':6} {xt(n, x, y):5.2f}")
print(f"{'yt: ':6} {yt(n, x, y):5.2f}")
print(f"{'Ixt: ':6} {Ixt(n, x, y):5.2f}")
print(f"{'Iyt: ':6} {Iyt(n, x, y):5.2f}")
print(f"{'Ixyt: ':6} {Ixyt(n, x, y):5.2f}")
