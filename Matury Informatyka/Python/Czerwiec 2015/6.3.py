kody = [
    10101110111010,
    11101010101110,
    10111010101110,
    11101110101010,
    10101110101110,
    11101011101010,
    10111011101010,
    10101011101110,
    11101010111010,
    10111010111010,
]

with open(r"C:\Users\zbysi\Desktop\Nowy folder\kody.txt") as f:
    for i in f:
        i = list(i)
        i.pop()

        parzyste = 0
        nieparzyste = 0
        suma = 0
        kod = 0
        zakodowane = "11011010"

        for j in range(0, len(i)):
            if j % 2 == 0:
                parzyste = parzyste + int(i[j])

            if j % 2 == 1:
                nieparzyste = nieparzyste + int(i[j])

        parzyste = parzyste * 3

        suma = parzyste + nieparzyste

        suma = suma % 10
        suma = 10 - suma
        suma = suma % 10

        kod = kody[suma]

        for j in range(0, len(i)):
            zakodowane = zakodowane + str(kody[int(i[j])])

        zakodowane = zakodowane + str(kod) + "11010110"

        print(int(zakodowane))
