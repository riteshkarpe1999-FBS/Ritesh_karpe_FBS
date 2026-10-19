###to Form a New String where the First Character and the Last Character have been Exchanged

str = input("Enter a string: ")

if len(str) <= 1:
    print(str)
else:
    str = str[-1] + str[1:-1] + str[0]
    print("New string:", str)



