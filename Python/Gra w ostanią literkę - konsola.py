import openpyxl

#Tworzenie pliku excela
# utwórz nowy arkusz i dodaj niektóre dane
workbook = openpyxl.Workbook()
worksheet = workbook.active

# zapisz arkusz do pliku
workbook.save("plik.xlsx")
workbook = openpyxl.load_workbook('plik.xlsx')
worksheet = workbook['Sheet']

#deklaracja podstawowych zmiennych
rundnik = 1
i = 0
stat = []


#funkcje odpowiedzailne za dobór kolorów
def czerwony(tekst):
    print(f'\033[91m{tekst}\033[0m')

def niebieski(tekst):
    print(f'\033[94m{tekst}\033[0m')


#funkcja odpowiedzialna za wyświetlanie statystyk
def staty():
    ilo = 0
    stat.sort()
    wynik = ""

    #sprawdza ile jest określonych znaków i taki jest przeskok
    while (ilo != len(stat)):
        wynik = wynik + str(stat[ilo] + str(stat.count(stat[ilo]))) + " "
        ilo = ilo + stat.count(stat[ilo])
    niebieski(wynik)


#Główny skrypt
while True:

    #iteracja
    i = int(i)
    i = i + 1
    i = str(i)

    #Pierwsze słowo
    if i == "1":
        slowo = input("Podaj pierwsze słówko: ")
        worksheet["A1"] = slowo.title()
        continue

    if slowo == "/break":
        break


    #Sekcja przypisywania liter i słów
    litera = worksheet["A" + str(int(i) - 1)].value[-1].upper()

    stat.append(litera)

    slowo = input(f"Podaj słówko na literkę {litera}: ").title()



    #Kontrola komend
    while slowo[0].title() != litera:

        if slowo == "/break".title():
            break

        if slowo == "/runda".title() and rundnik == 1:
            niebieski(f"Jest to {str(int(i) - 1)} słowo")
            slowo = input(f"Podaj słówko na literkę {litera}: ").title()
            rundnik = 0
            continue

        if slowo == "/staty".title() and rundnik == 1:
            staty()
            slowo = input(f"Podaj słówko na literkę {litera}: ").title()
            rundnik = 0
            continue


        #Pierwszy błąd jeżeli pętla się wykona
        czerwony(f"Błąd: Słowo musi rozpoczynać się od litery {litera}")
        slowo = input(f"Podaj słówko na literkę {litera}: ").title()


    #Kontrola powtarzalności
    okej = 0
    while okej != 1:
        ok = 1
        for j in range(1, int(i)):
            #przemierzenie całego stosu w poszukiwania odpowiednika
            if worksheet["A" + str(j)].value == slowo:
                czerwony(f"Błąd: Słowo zostało już wymienione w {j} turze")
                slowo = input(f"Podaj słówko na literkę {litera}: ").title()

                while slowo[0].title() != litera:
                    czerwony(f"Błąd: Słowo musi rozpoczynać się od litery {litera}")
                    slowo = input(f"Podaj słówko na literkę {litera}: ").title()

                ok = 0
                break

        if ok == 1:
            okej = 1


    if slowo == "/break".title():
        break

    worksheet["A"+i] = slowo.title()

    #Odniesienie do komend
    rundnik = 1


#Podsumowanie
print(f"\n gra zajeła {i} rund, statystyki były następujące ")
staty()

workbook.save('plik.xlsx')









