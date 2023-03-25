with open(r"C:\Users\zbysi\Desktop\Nowy folder\liczby.txt") as f:
    tab = []
    for i in f:
        tab.append(int(i))

count = 0
tab.sort()

for a in range(0, len(tab)):
    for b in range(a + 1, len(tab)):
        if tab[b] % tab[a] == 0:
            for c in range(b + 1, len(tab)):
                if tab[c] % tab[b] == 0:
                    for d in range(c + 1, len(tab)):
                        if tab[d] % tab[c] == 0:
                            for e in range(d + 1, len(tab)):
                                if tab[e] % tab[d] == 0:
                                    print(tab[a], tab[b], tab[c], tab[d], tab[e])
