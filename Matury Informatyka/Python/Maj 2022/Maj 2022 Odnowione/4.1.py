with open(r"C:\Users\zbysi\Desktop\Nowy folder\liczby.txt") as f:
    count = 0
    for i in f:
        x = list(i)
        x.pop()

        if x[0] == x[-1]:
            print(i)
            count = count + 1

print(count)
