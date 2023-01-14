with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2021\instrukcje.txt") as f:
    tab = []
    maxi = 0
    war = ""

    for i in f:
        if i[0] == "D":
            tab.append(i[-2])


for j in range(65, 91):
    count = tab.count(chr(j))

    if count > maxi:
        maxi = count
        war = chr(j)

print(maxi)
print(war)



