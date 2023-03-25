with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2017\punkty.txt") as f:
    count = 0
    for i in f:
        tab1 = set()
        tab2 = set()
        i = i.split(" ")

        x1 = list(i[0])
        x2 = list(i[1])
        x2.pop()

        for j in x1:
            tab1.add(j)

        for j in x2:
            tab2.add(j)

        if tab1 == tab2:
            count = count + 1


print(count)
