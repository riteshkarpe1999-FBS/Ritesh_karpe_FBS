### to check if given number is Armstrong or not using recursive function                                                                                                                                                                                                                                                                                                                                                                   Armstrong or not using recursive function.

def count(n):

    if n == 0:
        return 0
    return 1 + count(n // 10)


def armstrong(n, d):
    if n == 0:
        return 0

    return (n % 10) ** d + armstrong(n // 10, d)


num = int(input("Enter number: "))

d = count(num)
sum = armstrong(num, d)

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")











