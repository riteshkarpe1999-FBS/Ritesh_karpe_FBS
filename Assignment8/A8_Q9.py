### to check if entered number is a palindrome or not.

def palindrome(n):
    rev = 0
    temp = n

    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10

    return temp == rev

n = int(input("Enter number: "))

if palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")


