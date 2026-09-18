### to find sum of digits using recursion.

def digit_sum(n):
    if n == 0:
        return 0

    return n % 10 + digit_sum(n // 10)


num = int(input("Enter number: "))
print("Sum =", digit_sum(num))



