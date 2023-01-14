with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2022\liczby.txt") as f:
    for i in f:
        black = 0

        for j in range(2, int(i)):
            if int(i) % j == 0:
                black = 1


        x = list(i)
        x.pop()

        long = len(x)
        wartosc = ""

        while(long!=0):
            long = long - 1
            wartosc = wartosc + x[long]

        for j in range(2, int(wartosc)):
            if int(wartosc) % j == 0:
                black = 1

        if black == 0:
            print(i)














