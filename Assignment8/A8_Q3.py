#to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
#b. 1!+ 2! + 3! + 4!+..... + n!
#c. 1^1 + 2^2 + 3^3+ ...... n^n

### a. 1+ 2 + 3 + 4+..... + n

def sum_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter n: "))

print("Sum =", sum_series(n))


### b. 1!+ 2! + 3! + 4!+..... + n!

def factorial_sum(n):
    fact = 1
    total = 0

    for i in range(1, n + 1):
        fact = fact * i
        total = total + fact

    return total


n = int(input("Enter n: "))
print("Sum =", factorial_sum(n))

### c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i ** i

    return total


n = int(input("Enter n: "))

print("Sum =", sum_series(n))

