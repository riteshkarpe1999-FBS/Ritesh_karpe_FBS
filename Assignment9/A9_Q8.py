### to check whether a number is prime or not using recursion.

def prime(n, i=2):
    if n < 2:
        return False

    if i * i > n:
        return True

    if n % i == 0:
        return False

    return prime(n, i + 1)


num = int(input("Enter number: "))

if prime(num):
    print("Prime Number")
else:
    print("Not Prime Number")





