with open(r"C:\Users\zbysi\Desktop\Nowy folder\galerie.txt") as f:
    tab = []
    for i in f:
        i = i.split(" ")
        i = i[0]

        tab.append(i)

tab.sort()

n = 0
print(tab)
while n < len(tab):
    print(tab[n], tab.count(tab[n]))
    n = n + tab.count(tab[n])

    
        