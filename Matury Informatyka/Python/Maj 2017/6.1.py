with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2017\przyklad.txt") as f:

    min = 255
    max = 0

    for i in f:
        i = i.split(" ")

        for j in i:
            if int(j) < min:
                min = int(j)

            if int(j) > max:
                max = int(j)

print(min, max)
