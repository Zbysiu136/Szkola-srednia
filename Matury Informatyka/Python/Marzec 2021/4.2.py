with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Marzec 2021\galerie.txt") as f:
    p_max = 0
    nazwa1 = ""

    p_min = 9999999
    nazwa2 = ""

    for i in f:
        i = str(i)

        i = i.split(" ")

        pole = 0
        ok = 0
        lokali = 0

        for j in range(2, 142):
            if int(i[j]) != 0:
                lokali = lokali + 1

            ok = ok + 1

            if ok == 1:
                a = int(i[j])

            if ok == 2:
                pole = pole + int(i[j]) *a
                ok = 0

        if pole > p_max:
            p_max = pole
            nazwa1 = i[1]

        if pole < p_min:
            p_min = pole
            nazwa2 = i[1]

        print(i[1]+" "+str(pole)+" "+str((lokali)/2))

print("Max: " +str(p_max)+" "+str(nazwa1))
print("Min: " +str(p_min)+" "+str(nazwa2))