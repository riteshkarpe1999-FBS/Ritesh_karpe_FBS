#### to Sort the List According to the Second Element in Sublist
### in build function
# li = [[1, 5], [3, 2], [4, 8], [2, 1]]

# li.sort(key=lambda x: x[1])

# print(li)



## without in build function

li = [[1, 5], [3, 2], [4, 8], [2, 1]]
for i in range(len(li)):
    for j in range(i + 1,len(li)):
        if li[i][1] > li[j][1]:
            temp = li[i]
            li[i] = li[j]
            li[j]= temp
            print(li)











