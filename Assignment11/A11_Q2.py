### to Merge Two Lists and Sort it

a= [2, 1, 4]
b = [3, 5, 6]

c = a + b 
for i in range (6):
    for j in range (i + 1, 6):
        if c[i] >  c[j]:
            temp = c[i]
            c[i] = c[j]
            c[j]= temp
            print("Merge and Sorted", c)

 

