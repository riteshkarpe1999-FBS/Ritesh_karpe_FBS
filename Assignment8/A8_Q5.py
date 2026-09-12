 ### Sum of all prime numbers between 1 to n

def prime(n):

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_prime(n):
    sum = 0

    for i in range(2, n + 1):
        if prime(i):
            sum = sum + i

    return sum

n = int(input("Enter n: "))
print("Sum =", sum_prime(n))






