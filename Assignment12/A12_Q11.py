## To Replace Every Blank Space with a Hyphen

str = input("Enter a string: ")
result = ""

for i in str:
    if i == " ":
        result += "-"
    else:
        result += i

print("New string:", result)



