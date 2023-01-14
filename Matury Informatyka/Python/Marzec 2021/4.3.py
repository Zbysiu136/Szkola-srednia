with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Marzec 2021\galerie.txt") as f:

    ok = 0
    pola = []
    l_lokali = 0
    lmax = 0
    lmin = 9999
    nazwa_min = ""
    nazwa_max = ""

    for i in f:
        i = i.split(" ")

        pola.clear()
        l_lokali = 0



        for j in range(2,142):
            if i[j] == "0":
                break

            i[j] = int(i[j])

            ok = ok + 1

            if ok == 1:
                pole = i[j]

            if ok == 2:
                pola.append(int(pole*i[j]))
                ok = 0

        for j in range(0, len(pola)):
            l_lokali = l_lokali + 1 / pola.count(pola[j])
            l_lokali = l_lokali


        if l_lokali > lmax:
            lmax = l_lokali
            nazwa_max = i[1]

        if l_lokali < lmin:
            lmin = l_lokali
            nazwa_min = i[1]


print("Max: "+str(nazwa_max)+" "+str(round(lmax)))
print("Min: "+str(nazwa_min)+" "+str(round(lmin)))



