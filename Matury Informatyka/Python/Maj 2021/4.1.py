with open(r"C:\Users\zbysi\Desktop\Nowy folder\instrukcje.txt") as f:
    kod = []
    for i in f:
        i = i.split(" ")

        instrukcja = i[0]
        znak = i[1][0]

        if instrukcja == "DOPISZ":
            kod.append(znak)

        if instrukcja == "USUN":
            kod.pop()

        if instrukcja == "ZMIEN":
            kod[-1] = znak

        if instrukcja == "PRZESUN":
            for j in range(0, len(kod)):
                if kod[j] == znak:
                    if kod[j] == "Z":
                        kod[j] == "A"
                        ok = 0

                    kod[j] == chr(ord(kod[j]) + 1)


print(len(kod))
