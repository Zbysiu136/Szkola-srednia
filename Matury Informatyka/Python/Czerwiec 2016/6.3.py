with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2016\liczby.txt") as f:

    count = 0
    for i in f:
        number = 0

        if int(i[-2]) == 2:
            if int(i[0: -2], 2) % 2 == 0:
                count = count + 1

print(count)



