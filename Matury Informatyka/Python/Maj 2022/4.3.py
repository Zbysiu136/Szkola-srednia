with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2022\liczby.txt") as f:
    tab = []
    count = 0

    Parametr = 2 # 1 lub 2

    for i in f:
        i = int(i)
        tab.append(i)


    tab.sort()
    tab.reverse()

    def trojka(opcja):
        licz = 0


        if opcja == 1:
            for i in tab:
                for j in tab:
                    if i % j == 0 and i != j:
                        for z in tab:
                            if j % z == 0 and j != z:
                                print(str(i) + " ," + str(j) + " ," + str(z))
                                licz = licz + 1



        if opcja == 2:
            for i in tab:
                for j in tab:
                    if i % j == 0 and i != j:
                        for z in tab:
                            if j % z == 0 and j != z:
                                for x in tab:
                                    if z % x == 0 and z != x:
                                        for y in tab:
                                            if x % y == 0 and x != y:
                                                print(str(i) + " ," + str(j) + " ," + str(z) + " ," + str(x) + " ," + str(y))
                                                licz = licz + 1
        print("Ilość "+str(licz))




trojka(Parametr)









