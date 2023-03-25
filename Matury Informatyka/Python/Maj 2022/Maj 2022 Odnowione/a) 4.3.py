with open(r"C:\Users\zbysi\Desktop\Nowy folder\przyklad.txt") as f:
    tab = []
    for i in f:
        tab.append(int(i))

count = 0
tab.sort()

for a in range(0, len(tab)):
    for b in range(a+1, len(tab)):
        if tab[b] % tab[a] == 0:
            for c in range(b+1, len(tab)):
                if tab[c] % tab[b] == 0:
                    print(tab[a], tab[b], tab[c])
                    count = count + 1

print(count)