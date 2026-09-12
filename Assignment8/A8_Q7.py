### to find sum of digits of a number.
def sum_digits(num):
    total = 0

    while num > 0:                   
        digit = num % 10
        total = total + digit
        num = num // 10
    return total


n = int(input("Enter number: "))

print("Sum =", sum_digits(n))







