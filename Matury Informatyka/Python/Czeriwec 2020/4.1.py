with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czeriwec 2020\pary.txt") as f:
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


    for i in f:

        i = i.split(" ")
        i = int(i[0])
        ok = 0

        if i % 2 == 1:
            continue

        for j in prime:
            if ok == 1:
                ok = 0
                break
            for x in prime:
                if j + x == i:
                    print(str(i)+" "+str(j)+" "+str(x))
                    ok = 1