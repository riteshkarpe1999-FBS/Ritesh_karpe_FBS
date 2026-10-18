
##in build function

# li = ["apple", "hi", "banana", "cat", "orange"]

# li.sort(key=len)

# print("Sorted List:", li)


     ##without in build function


li = ["apple", "hi", "banana", "cat", "orange"]


for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if len(li[i]) > len(li[j]):
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
print("sortedlist",li)







