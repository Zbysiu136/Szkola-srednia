with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Kwiecień 2020\dane4.txt") as f:

    before = False
    times = 1
    r = 0
    rmax = 0
    maxi = 0

    for i in f:
        i = int(i)

        if r == abs(before - i):
            times = times + 1
            if times > rmax:
                rmax = times
                maxi = r

        else:
            times = 1

        if before == False:
            print(i, "start", times)
            before = i
            continue

        r = abs(before - i)

        print(i, r, times)

        before = i


print(rmax, maxi)
