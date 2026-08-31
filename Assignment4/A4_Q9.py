### WAP to print all numbers in a range divisible by a given number

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
divisor = int(input("Enter the divisor: "))

print(f"Numbers divisible by {divisor} between {start} and {end} are:")

for num in range(start, end + 1):
    if num % divisor == 0:
        print(num)











