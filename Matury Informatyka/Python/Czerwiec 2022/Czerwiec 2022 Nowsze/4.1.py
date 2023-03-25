with open(r"C:\Users\zbysi\Desktop\Nowy folder\liczby.txt") as f:
    for i in f:
        odbicie = ""
        i = list(i)
        i.pop()

        for j in range(0, len(i)):
            odbicie = odbicie + i[j*(-1) -1]
        
        if int(odbicie) % 17 == 0:
            print(odbicie)