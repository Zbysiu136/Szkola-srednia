with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2022\liczby.txt"
          r"") as f:
    tab = []
    suma = 0
    for i in f:
        tab.append(int(i))

    for j in range(0, len(tab)):
        print(tab.count(tab[j]))

        if tab.count(tab[j]) == 3:
            suma = suma + 1/3


    print("\n suma jednorazowych: "+str(suma))






