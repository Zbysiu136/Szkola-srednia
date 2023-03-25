with open(r"C:\Users\zbysi\Desktop\Nowy folder\napisy.txt") as f:
    count = 0
    for i in f:
        i = list(i)
        i.pop()
        if len(i) == 0:
            break

        ok = 1
        for j in range(1, 25):
            if i[j] != i[j * (-1)]:
                ok = 0

        if ok == 1:
            print(i[25])
    

        ok = 1


        for j in range(0, 24):
            if i[j] != i[j * (-1)-2]:

                ok = 0

        if ok == 1:
            print(i[24])
