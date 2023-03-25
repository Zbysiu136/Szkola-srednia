with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2016\liczby.txt") as f:

    suma = 0
    for i in f:
        if int(i[-2]) == 8:
            suma = suma + int(i[0: -2], 8)
            

print(suma)