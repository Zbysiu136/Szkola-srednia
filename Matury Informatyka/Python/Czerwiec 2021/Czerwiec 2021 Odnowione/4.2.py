with open(r"C:\Users\zbysi\Desktop\Nowy folder\przyklad.txt") as f:
    tab = []
    napis = ""
    for i in f:
        i = list(i)
        i.pop()

        tab.append(i)


n = 0
for i in range(19, 1000, 20):
    napis = napis + tab[i][n]
    n = n + 1

    
    
print(napis)