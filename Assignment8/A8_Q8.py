### find reverse of a number
def reverse_number(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return rev

n = int(input("Enter number: "))

print("reverse =", reverse_number(n))



