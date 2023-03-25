tab = []

for i in range(2, 10000):
    for j in range(2, 10000):
        if i == j:
            tab.append(i)
            break

        if i % j == 0:
            break

print(tab)
