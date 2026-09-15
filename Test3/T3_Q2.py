### the sum of following series

import math

# Input from user
n = int(input("Enter the value of n: "))

# Initialize sum
S = 0

# Loop through terms
for i in range(1, n + 1):
    S += i / math.factorial(i)

# Print result
print("Sum of series =", S)
