with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2021\napisy.txt") as f:
    count = 0

    for i in f:
        x = list(i)
        x.pop()

        for j in x:

            if j == "1" or j == "2" or j == "3" or j == "4" or j == "5" or j == "6" or j == "7" or j == "8" or j == "9" or j == "0":
                count = count + 1

print(count)