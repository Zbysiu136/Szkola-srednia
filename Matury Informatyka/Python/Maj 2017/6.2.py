with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2017\dane.txt") as f:
    ok = 0
    for i in f:
        i = i.split(" ")

        print(i)

        for j in range(0, 160):
            if int(i[j]) != int(i[j * (-1) - 1]):
                ok = ok + 1
                break


print(ok)
