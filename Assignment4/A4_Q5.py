## WAP to print Fibonacci series upto n
n = input("Enter a number:")
n = int(n)
a = 0
b = 1
print(a, b, end=" ")
for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c







