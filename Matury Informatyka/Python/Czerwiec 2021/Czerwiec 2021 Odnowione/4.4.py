with open(r"C:\Users\zbysi\Desktop\Nowy folder\napisy.txt") as f:
    count = 0
    ciag = ""
    for i in f:
        cyfry = ""
        ok = 0
        i = list(i)

        for j in range(0, len(i)):

            if (
                i[j] == "0"
                or i[j] == "1"
                or i[j] == "2"
                or i[j] == "3"
                or i[j] == "4"
                or i[j] == "5"
                or i[j] == "6"
                or i[j] == "7"
                or i[j] == "8"
                or i[j] == "9"
            ):
                ok = ok + 1
                cyfry = cyfry + i[j]

            if ok == 2:

                liczba = int(cyfry)
                if liczba >= 65 and liczba <= 90:
                    ciag = ciag + chr(liczba)

                    if liczba == 88:
                        count = count + 1

                cyfry = ""
                ok = 0
    
        if count == 3:
            break

print(ciag)