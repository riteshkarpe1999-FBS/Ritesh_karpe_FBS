
####  Print 1 to 100 in snakes and ladder pattern.


n = 1

for i in range(10):
    li = []

    for j in range(10):
        li.append(n)
        n += 1

    if i % 2 == 1:
        li.reverse()

    print(*li)




