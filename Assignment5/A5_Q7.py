#Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + .....n!
#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
#    d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
#e. x - x2/3 + x3/5 - x4/7 + .... to n term

###  a. 1! + 2! + 3! + 4! + .....n

n = int(input("Enter n: "))
s = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    s = s + fact
print(s)

### N + N^2 + N^3+N^4 .....+N^N

n = int(input("Enter n:"))
sum = 0

for i in range(1,n + 1):
    sum = sum + n ** i
    print("sum = ", sum)

### c. Find the sum of a geometric series from 1 to n where the common ratio is 2

n = int(input("Enter n: "))
s = 0
term = 1

for i in range(n):
    s = s + term
    term = term * 2

print(s)


#### d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter a: "))
s = 0
for i in range(1 , 11): 
 s = s + a ** i / i
 print(s)



#e. x - x2/3 + x3/5 - x4/7 + .... to n term


x = int(input("Enter x: "))
n = int(input("Enter n: "))
s = 0

for i in range(1, n + 1):
    term = x ** i / (2 * i - 1)

    if i % 2 == 0:
        s = s - term
    else:
        s = s + term

print(s)



