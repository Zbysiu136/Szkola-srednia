with open(r"C:\Users\zbysi\Desktop\Nowy folder\instrukcje.txt") as f:
    kod = []
    maxi = 0
    l = ""

    a = 0
    b = 0
    c = 0
    d = 0

    for i in f:
        i = i.split(" ")

        instrukcja = i[0]
        znak = i[1][0]

        if instrukcja == "DOPISZ":
            kod.append(znak)
           
            a = a + 1
            b = 0
            c = 0
            d = 0

        if instrukcja == "USUN":
            kod.pop()
            
            a = 0
            b = b + 1
            c = 0
            d = 0

        if instrukcja == "ZMIEN":
            kod[-1] = znak

            a = 0
            b = 0
            c = c + 1
            d = 0

        if instrukcja == "PRZESUN":
            for j in range(0, len(kod)):
                if kod[j] == znak:
                    if kod[j] == "Z":
                        kod[j] == "A"
                        ok = 0

                    kod[j] == chr(ord(kod[j]) + 1)
            
            a = 0
            b = 0
            c = 0
            d = d + 1
        
        print(a, b, c, d)


        if a > maxi:
            maxi = a
            l = "DOPISZ"
        
        if b > maxi:
            maxi = b
            l = "USUN"
        
        if c > maxi:
            maxi = c
            l = "ZMIEN"
        
        if d > maxi:
            maxi = d
            l = "PRZESUN"

            


print(maxi, l)
