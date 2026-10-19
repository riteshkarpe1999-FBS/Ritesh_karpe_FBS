
### To Count Lowercase Characters in a String

str = input("Enter a string: ")
count = 0

for i in str:
    if i >= 'a' and i <= 'z':
        count += 1

print("Lowercase characters:", count)







