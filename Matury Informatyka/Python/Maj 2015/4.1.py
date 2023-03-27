with open(r"C:\Users\zbysi\Desktop\Nowy folder\liczby.txt") as f:
    count = 0
    for i in f:
        i = list(i)
        i.pop()

        if i.count("0") > i.count("1"):
            count = count + 1

print(count)