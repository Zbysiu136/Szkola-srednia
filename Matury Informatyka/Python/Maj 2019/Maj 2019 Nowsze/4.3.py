with open(r"C:\Users\zbysi\Desktop\Nowy folder\liczby.txt") as f:
    tab = []
    dzielniki = []
    count = 1
    ciag = set()

    for i in f:
        tab.append(int(i))

for i in range(0, len(tab)):
    dzielnik = set()

    for j in range(2, tab[i] + 1):
        if tab[i] % j == 0:
            dzielnik.add(j)

    dzielniki.append(dzielnik)

ciag = dzielniki[0]

for i in range(1, len(dzielniki)):
    ciag = ciag.intersection(dzielniki[i])

    count = count + 1
    if len(ciag) == 0:
        ciag = dzielniki[i]
        count = 1

    print(i, tab[i], count, ciag)

#Problem taki iż, jeżeli w poprzedniej liczbie znalazły się wspólne dzielniki to jest to zaliczane do ciągu poprzedniego pomimo że 
#w następnej linijce mogły być wspólne dzielniki również