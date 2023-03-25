with open(r"C:\Users\zbysi\Desktop\Nowy folder\liczby.txt") as f:
    tab = []
    jeden = 0
    dwa = 0
    trzy = 0
    for i in f:
        tab.append(int(i))

tab.sort()

n = 0
while n < len(tab):
    a = tab.count(tab[n])

    if a == 1:
        jeden = jeden + 1

    if a == 2:
        dwa = dwa + 1

    if a == 3:
        trzy = trzy + 1

    n = n + a

print(jeden+dwa+trzy, dwa, trzy)
