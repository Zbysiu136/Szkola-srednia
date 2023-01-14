with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Lipiec 2020\identyfikator.txt") as f:
    suma_max = 0
    nazwa = ""

    for i in f:

        suma = 0


        x = i[3:9]

        for j in x:
            suma = int(j) + suma

        if suma >= suma_max:
            suma_max = suma
            nazwa = i

            print(suma)
            print(i)

print(nazwa)