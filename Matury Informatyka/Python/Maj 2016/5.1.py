with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2016\gra.txt") as f:
    plansza = []
    for i in f:

        i = list(i)
        i.pop()
        plansza.append(i)
        count = 0

for i in range(0, 12):
    count = 0
    for j in plansza[i]:
        count = count + 1
        if j == "X":
            print("Linijka "+str(i+1)+" "+"Kolumna "+str(count))
