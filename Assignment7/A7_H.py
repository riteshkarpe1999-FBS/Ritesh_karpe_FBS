### Double symmetric number wings

n = 5
for i in range(1, n + 1):
    # Left numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Middle spaces
    print(" " * ((n - i) * 4), end="")
    
    # Right numbers
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()





