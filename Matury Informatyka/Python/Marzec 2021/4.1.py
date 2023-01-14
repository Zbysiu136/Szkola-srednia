with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Marzec 2021\galerie.txt") as f:
    tab = []
    rab = []

    for i in f:

        i = i.split(" ")
        print(i)

        tab.append(i[0])

print(tab)
for i in range(0, len(tab)):
    rab.append(tab[i]+" "+ str(tab.count(tab[i])))

rab = set(rab)

print(rab)