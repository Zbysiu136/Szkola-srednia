tab = []

for i in range(2, 100):

    ok = 0
    for j in range(2, 100):
        if i == j:
            continue
        if i % j == 0:
            ok = 1

    if ok == 0:
        tab.append(i)


print(tab)
