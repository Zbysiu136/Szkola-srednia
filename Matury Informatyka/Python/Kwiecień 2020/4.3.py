with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Kwiecień 2020\dane4.txt") as f:

    before = False
    times = 1
    r = 0
    rmax = 0
    maxi = 0
    rs = []

    for i in f:
        i = int(i)

        if r == abs(before - i):
            times = times + 1

        else:
            times = 1

        if before == False:
            print(i, "start", times)
            before = i
            continue

        r = abs(before - i)

        print(i, r, times)

        before = i

        rs.append(r)

print(rs)
rs = sorted(rs)

tab = []
n = 0
while(n != len(rs)-1):
    tab.append(str(rs[n])+" "+str(rs.count(rs[n])))
    n = n + rs.count(rs[n])
    


print(rs)
print(tab)

for i in tab:
    i = i.split()
    if i[1] == "1":
        continue
    print(i)