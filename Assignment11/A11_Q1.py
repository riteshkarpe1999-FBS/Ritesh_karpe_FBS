##  to Put Even and Odd elements of a List into two Different list
a=[10, 15, 20, 25, 30 ,35]

even = []
odd = []
for i in a:
    if i % 2 == 0 :
        even = even  + [i]
    else:
        odd = odd + [i]
print("Even list ", even)
print("odd  list ", odd)









