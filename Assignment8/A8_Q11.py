### to check if a given number is Armstrong number or not For each task create separate functions
def armstrong(n):
    temp = n
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** 3
        n = n // 10

    return total == temp


n = int(input("Enter number: "))

if armstrong(n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")











