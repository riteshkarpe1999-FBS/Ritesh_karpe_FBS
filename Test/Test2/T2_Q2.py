
# Program to check special 3-digit condition

num = int(input("Enter a 3-digit number: "))


first = num // 100        
second = (num // 10) % 10 
third = num % 10          

if first == 2 * second and first == third // 2 and third % 2 == 0:
    print("Yes, you have done it")
else:
    print("Please try next time")






