# Program to check whether an alphabet is vowel or consonant

# Input from user
ch = input("Enter an alphabet: ")
# Check if input is a single alphabet
if len(ch) == 1 and ch.isalpha():
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print(f"{ch} is a vowel.")
    else:
        print(f"{ch} is a consonant.")
else:
    print("Invalid input! Please enter a single alphabet.")





















