with open(r"C:\Users\zbysi\Desktop\Nowy folder\liczby.txt") as f:
    dwa = 0
    osiem = 0

    for i in f:
        i = list(i)

        if i[-2] == "0":
            dwa = dwa + 1
    
        if i[-4: -1].count("1") == 0:
            osiem = osiem + 1

print("dwa:",dwa, "osiem:",osiem)
