with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Maj 2019\przyklad.txt") as f:
    dzielniki = set()
    dzielniki_p = set()
    ok = 0
    pierwsza_cyfra_ciagu = 0
    count = 1
    c_max = 0

    for i in f:
        if ok == 0:
            i = int(i)

            pierwsza_cyfra_ciagu = i
            for j in range(2, i + 1):
                if i % j == 0:
                    dzielniki_p.add(j)
                    ok = 1

            continue


        i = int(i)
        count = count + 1

        for j in range(2, i+1):
            if i % j == 0:
                dzielniki.add(j)

        dzielniki_p = dzielniki_p.intersection(dzielniki)


        dzielniki.clear()

        if len(dzielniki_p) == 0:

            pierwsza_cyfra_ciagu = i

            if count > c_max:
                c_max = count
                print(pierwsza_cyfra_ciagu, count - 1)

            count = 1

            dzielniki_p.clear()
            dzielniki_p = dzielniki














