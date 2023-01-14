with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2016\gra.txt") as f:
    plansza = []
    for i in f:
        i = list(i)
        i.pop()

        for j in i:
            plansza.append(j)

count = 1
kolumna = 1
for i in plansza:

    print(i)
    count = count +1
    if count == 21:
        print("\n")
        count = 1
        kolumna = kolumna + 1

    print(count)