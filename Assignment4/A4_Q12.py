### Write a program to check if given number is Armstrong number or not

num = int(input("Enter a number: "))
digits = len(str(num))
sum = sum(int(digit) ** digits for digit in str(num))

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")





















