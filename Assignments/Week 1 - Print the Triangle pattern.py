# Create lower triangular, upper triangular and pyramid containing the "*" character.

n = 5  # number of rows

print("Lower Triangular Pattern")
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("\nUpper Triangular Pattern")
for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()

print("\nPyramid Pattern")
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))
