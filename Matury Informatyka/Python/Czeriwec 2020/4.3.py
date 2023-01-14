with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czeriwec 2020\pary.txt") as f:
    for i in f:
        i = i.split(" ")

        liczba = i[0]
        slowo = i[1]

        if int(liczba) == len(slowo)-1:
            print(liczba + " " + slowo)