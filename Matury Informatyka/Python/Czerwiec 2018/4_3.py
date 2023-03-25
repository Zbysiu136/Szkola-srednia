F = []
G = []
tab = []

with open(r'C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2018\przyklad1.txt') as f:
    for i in f:
        i = i.split(" ")

        F.append(i)


with open(r'C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2018\przyklad2.txt') as g:
    for i in g:
        i = i.split(" ")

        G.append(i)



for i in range(0, len(F)):
    a = 0
    b = 0
    print(tab)
    tab = []

    for j in range(0, len(F[i])+len(G[i])):

        print(j)
        print(a,b)



        if a == len(F[i]):
            for x in range(b, len(G[i])):
                tab.append(int(G[x]))
                print("Łamię")
            break

        if b == len(G[i]):
            for x in range(a, len(F[i])):
                tab.append(int(F[x]))
                print("Łamię")
            break



        if int(F[i][a]) < int(G[i][b]):

            tab.append(int(F[i][a]))
            a = a + 1
            continue

        if int(G[i][b]) < int(F[i][a]):
            tab.append(G[i][b])
            b = b + 1
            continue

        if int(G[i][b]) == int(F[i][a]):
            tab.append(G[i][b])
            tab.append(G[i][b])
            a = a + 1
            b = b + 1
            continue


    print("##########")






