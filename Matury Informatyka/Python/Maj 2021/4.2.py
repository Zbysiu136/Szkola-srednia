with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2021\instrukcje.txt") as f:
    last = "x"
    count = 0
    maxi = 0
    war = ""

    for i in f:


        if i[0] == last:
            count = count + 1
            if count > maxi:
                maxi = count
                war = i

        if i[0] != last:
            count = 0


        last = i[0]




print(maxi)
print(war)
