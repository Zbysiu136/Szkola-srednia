with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2021\instrukcje.txt") as f:
    count = 0

    for i in f:
        x = list(i)

        if x[0] == "D":
            count = count + 1

        if x[0] == "U":
            count = count - 1

print(count)