with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2022\liczby.txt") as f:
    max_wynik = 0
    for i in f:
        x = list(i)
        x.pop()

        long = len(x)
        wartosc = ""

        while(long!=0):
            long = long - 1
            wartosc = wartosc + x[long]

        wynik = abs(int(i)-int(wartosc))

        if max_wynik < wynik:
            max_wynik = wynik
            max_liczba = i


print(max_wynik)
print(max_liczba)

