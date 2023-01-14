with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Lipiec 2020\identyfikator.txt") as f:
    for i in f:

        oryginal = i
        i = list(i)
        i.pop()
        ciag = []

        pow = 0

        for j in i:

            if pow == 3:
                kont = j


            if pow > 3:
                ciag.append(int(j))

            count = 0
            for x in range(65, 91):

                if chr(x) == j:
                    ciag.append(10+count)
                    break
                count = count + 1


            pow = pow + 1


        suma = 0
        suma = ciag[0]*7 + ciag[1]*3 + ciag[2]*1 + ciag[3]*7 + ciag[4]*3 + ciag[5]*1 + ciag[6]*7 + ciag[7]*3


        if suma % 10 != int(kont):
            print(oryginal)