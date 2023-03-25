with open(r"C:\Users\zbysi\Desktop\Nowy folder\kody.txt") as f:
    for i in f:
        i = list(i)
        i.pop()

        parzyste = 0
        nieparzyste = 0

        for j in range(0, len(i)):
            if j % 2 == 0:
                parzyste = parzyste + int(i[j])
            
            if j % 2 == 1:
                nieparzyste = nieparzyste + int(i[j])
        
        print(parzyste, nieparzyste)

