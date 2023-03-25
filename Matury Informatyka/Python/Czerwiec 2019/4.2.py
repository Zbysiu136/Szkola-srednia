with open(
    r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2019\pierwsze.txt"
) as f:
    for i in f:
        ok = 1
        l = ""

        x = list(i)

        x.pop()

        for j in range(len(x) - 1, -1, -1):
            l = l + x[j]

        l = int(l)

        for j in range(2, l):
            if l % j == 0:
                ok = 0

        if ok == 1:
            print(i)
