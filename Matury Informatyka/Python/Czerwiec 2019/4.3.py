with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2019\pierwsze.txt") as f:

    def Suma(j):
        suma = 0
        j = str(j)

        x = list(j)

        for n in x:
            suma = suma + int(n)

        if suma >= 10:
            Suma(suma)

        if suma == 1:
            print("ok")

    for i in f:
        i = int(i)
        Suma(i)
