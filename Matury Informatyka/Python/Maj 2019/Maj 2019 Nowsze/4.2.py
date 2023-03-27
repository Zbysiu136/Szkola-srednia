with open(r"C:\Users\zbysi\Desktop\Nowy folder\liczby.txt") as f:
    for i in f:
        x = list(i)
        x.pop()

        suma = 0
        sumy = 0

        for j in range(0, len(x)):
            liczba = int(x[j])

            sumy = liczba
            liczba = liczba - 1
            if liczba <= 0:
                sumy = 1

            while liczba > 0:
                sumy = sumy * liczba
                liczba = liczba - 1
            
            suma = suma + sumy
        
        if suma == int(i):
            print(i)
            
