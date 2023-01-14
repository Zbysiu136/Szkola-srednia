tab = {}
zab = []

for i in range(2, int(10000/2+1)):
    for j in range(2, int(10000/2+1)):
        if i % j == 0:
            break


    tab[j] = j

for i in tab:
    zab.append(i)

print(zab)