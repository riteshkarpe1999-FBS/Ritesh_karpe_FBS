###   to Find the Second Largest Number in a List Using Bubble

li=[50, 30, 70, 40, 20, 10]


# Bubble Sort in descending order
for i in range(len(li)):
    for j in range(0, len(li) - i - 1):
        if li[j] < li[j + 1]:
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp

print("Sorted List:", li)
print("Second Largest Number:", li[1])









