with open(r"C:\Users\zbysi\Desktop\Nowy folder\liczby.txt") as f:
    maxi = 0
    l = ''
    for i in f:
        odbicie = ""
        x = list(i)
        x.pop()

        for j in range(0, len(x)):
            odbicie = odbicie + x[j*(-1) -1]
        
        r = abs(int(i) - int(odbicie))

        if r > maxi:
            maxi = r
            l = i

print(l, maxi)
