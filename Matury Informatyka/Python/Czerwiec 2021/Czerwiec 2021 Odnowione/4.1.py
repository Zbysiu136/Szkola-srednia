with open(r"C:\Users\zbysi\Desktop\Nowy folder\napisy.txt") as f:
    count = 0
    suma = 0
    for i in f:
        i = list(i)

        for j in range(0, len(i)):
            if (
                i[j] == "0"
                or i[j] == "1"
                or i[j] == "2"
                or i[j] == "3"
                or i[j] == "4"
                or i[j] == "5"
                or i[j] == "6"
                or i[j] == "7"
                or i[j] == "8"
                or i[j] == "9"
            ):
                count = count + 1

        print(count)

        suma = suma + count
        count = 0

print(suma)
