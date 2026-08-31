### WAP to check if given number Strong Number
n = int(input("Enter a number: "))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum += fact
    n //= 10

if sum == temp:
    print("Strong Number")
else:
    print("Not Strong Number")













