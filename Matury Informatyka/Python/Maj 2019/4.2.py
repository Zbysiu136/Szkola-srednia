with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2019\liczby.txt") as f:
    for i in f:
        x = list(i)
        x.pop()

        licznik = 1
        suma = 0

        for o in x:
            for j in range(1, int(o)+1):
                licznik = licznik * j

            suma = suma + licznik
            licznik = 1

        if str(suma)+"\n" == i:
            print(i)


