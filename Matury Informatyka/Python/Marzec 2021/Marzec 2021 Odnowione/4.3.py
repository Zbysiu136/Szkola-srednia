with open(r"C:\Users\zbysi\Desktop\Nowy folder\galerie.txt") as f:
    powierzchnia = 0
    count = 0
    maxi = 0
    mini = 9999999999999
    l_min = ""
    l_max = ""
    unikatowe = 0
    tab = set()

    for i in f:
        i = i.split(" ")
        x = i[1]
        i = i[2 : len(i)]

        tab = set()
        unikatowe = 0

        for j in range(0, 140, 2):
            if i[j] == "0":
                break

            powierzchnia = int(i[j]) * int(i[j + 1])
            tab.add(powierzchnia)

        unikatowe = len(tab)

        if unikatowe > maxi:
            maxi = unikatowe
            l_max = x

        if unikatowe < mini:
            mini = unikatowe
            l_min = x


print("Max", l_max, maxi, "Min:", l_min, mini)
