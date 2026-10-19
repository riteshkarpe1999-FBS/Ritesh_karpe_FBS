#####  Python Program to Replace all Occurrences of ‘a’ with $ in a String

str1 = (input("Enter the string:"))

str2 =""
for i in (str1):
    if i == "a":

        str2 = str2 + "$"
    else:
        str2 = str2 + i 
        print("updated string",str2)



