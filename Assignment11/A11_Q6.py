###  to Find the Union of two Lists

a=[1, 2, 3, 4, 5]
b=[3, 4, 5, 6, 7, 8]

union=[]
for i in a:
    if i not in union:
        union.append(i)

for i in b:
    if i not in union:
        union.append(i)

print("Union of two lists:", union)
