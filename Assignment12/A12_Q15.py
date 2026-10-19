## TO Find the Larger String Without Built-in Functions


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

count1 = 0
count2 = 0

for i in s1:
    count1 += 1

for i in s2:
    count2 += 1

if count1 > count2:
    print(s1, "is larger")
elif count2 > count1:
    print(s2, "is larger")
else:
    print("Both strings are equal in length")



