with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2016\liczby.txt") as f:

    suma = 0
    maxi = 0
    mini = 999
    maxil = ""
    minil = ""
    for i in f:

        system = int(i[-2])
        liczba = int(i[0:-2], system)

        if liczba > maxi:
            maxi = liczba
            maxil = int(i)
            print(int(i), liczba)

        if liczba < mini:
            mini = liczba
            minil = int(i)
            print(int(i), liczba)


print("max:", maxil, "min", minil)
