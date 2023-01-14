with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2022\liczby.txt") as f:
    tab = []
    suma = 0
    for i in f:
        tab.append(int(i))

    for j in range(0, len(tab)):
        print(tab.count(tab[j]))
        if tab.count(tab[j]) == 1:
            suma = suma + 1
        if tab.count(tab[j]) > 1:
            suma = suma + 1/tab.count(tab[j])

    print("\n suma jednorazowych: "+str(suma))






