with open(r"C:\Users\zbysi\Desktop\Nowy folder\liczby.txt") as f:
    maxi = 0
    mini = 999999999999999999999
    count = 1

    for i in f:
        i = int(i, 2)

        if i >= maxi:
            maxi = i
            print("Max", count)

        if i <= mini:
            mini = i
            print("min", count)

        count = count + 1
