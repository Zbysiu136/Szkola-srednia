with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2021\Test.txt") as f:
    napis = []
    nap = ""

    for i in f:
        print(napis)
        print(i[-2])

        if i[0] == "D":
            napis.append(i[-2])

        if i[0] == "U":
            for d in range(1, len(napis)):
                if napis[d * (-1)] != "":
                    napis[d * (-1)] = ""



        if i[0] == "Z":
            napis[-1] = ""
            napis.append(i[-2])

        if i[0] == "P":
            print(napis)
            print(i[-2])
            print(napis.count(i[-2]))
            if napis.count(i[-2]) > 0:
                napis[napis.index(i[-2])] = chr(ord(i[-2])+1)

        print(napis)




for j in napis:
    nap = nap + j

napis = nap
print(napis)