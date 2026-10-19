###  to Detect if Two Strings are Anagrams

## with in in build function 


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.lower()
str2 = str2.lower()

if sorted(str1) == sorted(str2):
    print("Strings are Anagrams")
else:
    print("Strings are not Anagrams")



## without in build function 


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.lower()
str2 = str2.lower()

if len(str1) != len(str2):
    print("Strings are not Anagrams")
else:
    for i in str1:
        count1 = 0
        count2 = 0

        for j in str1:
            if i == j:
                count1 += 1

        for j in str2:
            if i == j:
                count2 += 1

        if count1 != count2:
            print("Strings are not Anagrams")
            break
    else:
        print("Strings are Anagrams")


