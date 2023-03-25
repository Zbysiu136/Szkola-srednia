with open(r"C:\Users\zbysi\Desktop\Nowy folder\galerie.txt") as f:
    suma = 0 
    count = 0
    maxi = 0
    mini = 9999999999999
    l_min = ""
    l_max = ""

    for i in f:
        i = i.split(" ")
        x = i[1]
        i = i[2:len(i)]
        

        for j in range(0, 140, 2):
            if i[j] == "0":
                break
            
            suma = suma + int(i[j]) * int(i[j+1])
            count = count + 1


        
        print(x, suma, count)
        if suma > maxi:
            maxi = suma
            l_max = x

        if suma < mini:
            mini = suma
            l_min = x
        
        suma = 0
        count = 0

print("Max",l_max,  maxi, "Min:",l_min, mini)