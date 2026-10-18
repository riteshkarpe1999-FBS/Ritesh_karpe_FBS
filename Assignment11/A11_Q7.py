
####  to Find the Intersection of Two Lists


a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

intersection = []

for i in a:
    if i in b and i not in intersection:
        intersection.append(i)

print("Intersection of two lists:", intersection)


