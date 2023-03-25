with open(r"C:\Users\zbysi\Desktop\Nowy folder\przyklad.txt") as f:
    kod = []
    tab = []

    maxi = 0
    for i in f:
        i = i.split(" ")

        instrukcja = i[0]
        znak = i[1][0]

        if instrukcja == "DOPISZ":
            kod.append(znak)
            tab.append(znak)

        if instrukcja == "USUN":
            kod.pop()

        if instrukcja == "ZMIEN":
            kod[-1] = znak

        if instrukcja == "PRZESUN":
            for j in range(0, len(kod)):
                if kod[j] == znak:
                    if kod[j] == "Z":
                        kod[j] == "A"
                        ok = 0

                    kod[j] == chr(ord(kod[j]) + 1)


tab.sort()

print(tab)

n = 0
while n < len(tab):
    if tab.count(tab[n]) > maxi:
        maxi = tab.count(tab[n])
        l = tab[n]

    
    n = n + tab.count(tab[n])

print(maxi, l)
    
    

    
    
