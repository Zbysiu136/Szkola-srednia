with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2022\przyklad.txt") as f:
    for i in f:
        x = list(i)
        x.pop()

        long = len(x)
        wartosc = ""

        while(long!=0):
            long = long - 1
            wartosc = wartosc + x[long]

        if int(wartosc) % 17 == 0:
            print(wartosc)

