with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2017\dane.txt") as f:
    tab = []
    count = 0
    maxi = 0
    for i in f:
        i = i.split(" ")

        tab.append(i)


for j in range(0, 320):
    if count > maxi:
        maxi = count

    count = 0

    for i in range(1, 200):
        if int(tab[i][j]) == int(tab[i - 1][j]):
            count = count + 1

        if int(tab[i][j]) != int(tab[i - 1][j]):
            if count > maxi:
                maxi = count

            count = 0


print(maxi+1)
