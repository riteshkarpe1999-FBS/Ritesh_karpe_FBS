# Program to find numbers divisible by 7 and multiple of 5 in a given range

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

print(f"Numbers divisible by 7 and multiple of 5 between {start} and {end} are:")

for num in range(start, end + 1):
    if num % 7 == 0 and num % 5 == 0:
        print(num)








