with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2021\napisy.txt") as f:
    count = 0
    poz = 0
    str = ""

    for i in f:
        count = count + 1

        if count % 20 == 0:
            x = list(i)

            str = str+x[poz]
            poz = poz+1

print(str)
