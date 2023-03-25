with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2017\dane.txt") as f:
    tab = []
    count = 0
    for i in f:
        i = i.split(" ")

        tab.append(i)


for i in range(0, 200):
    for j in range(0, 320):
        x1 = 0
        x2 = 0
        x3 = 0
        x4 = 0

        if i == 199:
            x1 = 1

        if i == 0:
            x2 = 1

        if j == 319:
            x4 = 1

        if j == 0:
            x3 = 1

        print(i, j, x1, x2, x3, x4)

        if x1 == 0:
            if abs(int(tab[i][j]) - int(tab[i + 1][j])) > 128:
                count = count + 1
                continue

        if x2 == 0:
            if abs(int(tab[i][j]) - int(tab[i - 1][j])) > 128:
                count = count + 1
                continue
       
        if x3 == 0:
            if abs(int(tab[i][j]) - int(tab[i][j - 1])) > 128:
                count = count + 1
                continue

        if x4 == 0:
            if abs(int(tab[i][j]) - int(tab[i][j + 1])) > 128:
                count = count + 1
                continue
            



print(count)
