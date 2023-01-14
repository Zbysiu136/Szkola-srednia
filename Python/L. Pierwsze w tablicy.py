tab = {}
zab = []

for i in range(2, int(10000/2+1)):
    for j in range(2, int(10000/2+1)):
        if i % j == 0:
            break


    tab[j] = j #Przypisanie wartości do słownika polega na wybraniu słowa(miejsca - [j]) a następnie przypisanie mu definicji(wartości - j),
    #wartości w słowniku nie mogą się powtarzać więć jeżeli dla tego samego próbujemy przypisać wartość zostanie ona zamieniona
    #Dla wypisania for i in słownik zostaną wypisane same słowa

for i in tab: #zostanie przypisane po kolei to tablicy słowa z słownika, bez definicji
    zab.append(i)

print(zab)