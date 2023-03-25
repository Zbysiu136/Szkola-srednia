with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2017\punkty.txt") as f:
    punkty = []
    dlugosc_max = 0
    for i in f:
        i = i.split(" ")
        i[0] = int(i[0])
        i[1] = int(i[1])
        punkty.append(i)


for i in range(0, len(punkty)):
    for j in range(0, len(punkty)):

        xa = punkty[i][0]
        ya = punkty[i][1]

        xb = punkty[j][0]
        yb = punkty[j][1]

        dlugosc = (xb - xa) * (xb - xa) + (yb - ya) * (yb - ya)
        if dlugosc > dlugosc_max:
            dlugosc_max = dlugosc

print(dlugosc_max)
