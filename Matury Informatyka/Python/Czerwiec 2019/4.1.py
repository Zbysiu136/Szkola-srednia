with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2019\liczby.txt") as f:
    for i in f:
        i = int(i)
        ok = 1

        if i >= 100 and i <= 5000:
            for j in range(2, i):
                if i % j == 0:
                    ok = 0
            
            if ok == 1:
                print(i)