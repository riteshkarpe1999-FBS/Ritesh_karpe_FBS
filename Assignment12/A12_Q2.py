##to Remove the nth Index Character from a Non-Empty string

str1 = input("Enter a string: ")
n = int(input("Enter index to remove: "))

str2 = ""

for i in range(len(str1)):
    if i != n:
        str2 = str2 + str1[i]

print("String after removing character:", str2)