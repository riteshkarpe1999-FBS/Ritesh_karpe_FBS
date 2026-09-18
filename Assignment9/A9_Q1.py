### 1! + 2! + 3! + 4! +..... + n!sum of following series using recursive functions:

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def series(n):
    if n == 0:
        return 0
    return fact(n) + series(n - 1)

n = int(input("Enter n: "))

print("Sum =", series(n))







