with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2016\liczby.txt") as f:

    count = 0
    for i in f:
        ok = 0
        if int(i[-2]) == 4:
            ok = 1
            for j in range(0, len(i)-1):
                if int(i[j]) == 0:
                    ok = 0
        
        if ok == 1:
            count = count + 1

print(count)