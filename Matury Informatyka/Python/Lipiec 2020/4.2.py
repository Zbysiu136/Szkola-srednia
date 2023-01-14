with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Lipiec 2020\identyfikator.txt") as f:
    for i in f:
        id = i[0:3]
        kod = i[3:9]

        ok = 0

        if id[0] == id[-1]:
            ok = 1

        if kod[0] == kod[-1] and kod[1] == kod[-2] and kod[2] == kod[-3]:
            ok = 1


        if ok == 1:
            print(i)


