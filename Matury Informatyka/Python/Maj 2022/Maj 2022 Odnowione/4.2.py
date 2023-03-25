with open(r"C:\Users\zbysi\Desktop\Nowy folder\liczby.txt") as f:

    unikatowe_max = 0
    suma_max = 0

    unikatowe_l = ""
    suma_l = ""

    for i in f:

        i = int(i)
        x = int(i)
        licznik = 2
        unikatowe = set()
        suma = 0

        while i != 1:
            if i % licznik == 0:
                i = i / licznik
                unikatowe.add(licznik)
                suma = suma + 1
                licznik = 1

            licznik = licznik + 1

        if len(unikatowe) >= unikatowe_max:
            unikatowe_max = len(unikatowe)
            print("Unikatowe",x, unikatowe_max)

        if suma >= suma_max:
            suma_max = suma
            print("Suma", x, suma_max)



