with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2021\napisy.txt") as f:

    for i in f:

        x = list(i)
        x.pop()
        x.append(x[0])

        black = 0

        for j in range(0, 26):
            if x[j] != x[j*(-1) -1]:
                black = 1
                break

        if black == 0:
            print(x[25])








