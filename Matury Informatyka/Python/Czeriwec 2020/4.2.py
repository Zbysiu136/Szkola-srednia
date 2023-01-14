with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czeriwec 2020\pary.txt") as f:
    for i in f:

        i = i.split(" ")
        i = i[1]
        wynik = 1
        wynik_max = 0
        znak = ""
        wynikowy = ""

        for j in range(0, len(i)-1):

            if i[j] == i[j+1]:
                wynik = wynik + 1

            if i[j] != i[j + 1]:
                if wynik > wynik_max:
                    wynik_max = wynik
                    znak = i[j]

                wynik = 1

        for j in range(0, wynik_max):
            wynikowy = wynikowy + znak

        wynikowy = wynikowy +" "+ str(wynik_max)

        print(wynikowy)
