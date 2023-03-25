with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2019\liczby.txt") as f:
    suma = 0

    for i in f:
        ok = 0
        for j in range(0, 11):
            if int(i) == pow(3, j):
                ok = 1
                break

        if ok == 1:
            suma = suma + 1

print(suma)


