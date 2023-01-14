with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2022\liczby.txt") as f:
    count = 0
    for i in f:


        x = list(i)
        x.pop()

        if x[0] == x[-1]:
            count = count + 1
            print(i)

    print(count)