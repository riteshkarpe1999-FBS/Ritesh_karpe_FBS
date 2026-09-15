
### Write a program to print pattern

n = 5   # number of rows
m = 5   # number of columns

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()



