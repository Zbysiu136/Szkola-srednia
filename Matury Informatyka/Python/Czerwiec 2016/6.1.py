with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2016\liczby.txt") as f:

    count = 0
    for i in f:
        if int(i[-2]) == 8:
            count = count + 1

print(count)
