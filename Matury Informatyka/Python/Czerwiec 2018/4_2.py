count = 0
I = []
J = []

with open(r'C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2018\dane1.txt') as f:
    for i in f:
        i = i.split(" ")
        a = 0
        b = 0

        for j in i:
            j = int(j)

            if j % 2 == 0:
                a = a + 1

            if j % 2 == 1:
                b = b + 1

        if a == 5 and b == 5:
            I.append(1)

        if a != 5 and b != 5:
            I.append(0)





with open(r'C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2018\dane2.txt') as g:
    for i in g:
        i = i.split(" ")
        a = 0
        b = 0

        for j in i:
            j = int(j)

            if j % 2 == 0:
                a = a + 1

            if j % 2 == 1:
                b = b + 1

        if a == 5 and b == 5:
            J.append(1)

        if a != 5 and b != 5:
            J.append(0)

for i in range(0, len(I)):
    if J[i] == 1 and I[i] == 1:
        count = count + 1
print(count)