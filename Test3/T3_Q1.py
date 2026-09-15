### Write a program to print first n prime numbers
n = int(input("Enter how many primes: "))
count = 0
num = 2

while count < n:
    for i in range(2, num+1):
        if num % i == 0:
            break
    if i == num:   # prime check
        print(num, end=" ")
        count += 1
    num += 1






