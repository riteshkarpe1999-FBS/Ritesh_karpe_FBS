### To Count the Occurrences of Each Word in a String


s = input("Enter a string: ")
words = s.split()
checked = []

for i in words:
    if i not in checked:
        count = 0

        for j in words:
            if i == j:
                count += 1

        print(i, ":", count)
        checked.append(i)

