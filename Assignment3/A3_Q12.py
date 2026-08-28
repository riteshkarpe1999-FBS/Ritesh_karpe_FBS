# Palindrome check for a 3-digit number

n = int(input("Enter a 3-digit number: "))

# Convert number to string
num_str = str(n)

# Check if the string is equal to its reverse
if num_str == num_str[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome number")

























