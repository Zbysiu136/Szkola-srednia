with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2017\punkty.txt") as f:
    a = 0
    b = 0
    c = 0

    for i in f:
        i = i.split(" ")
        x = int(i[0])
        y = int(i[1])


        if x < abs(5000) and y < abs(5000):
            a = a + 1
        
        if abs(y) == 5000 and abs(x) < 5000:
            b = b + 1
        
        if abs(x) == 5000 and abs(y) < 5000:
            b = b + 1
        
        if x > abs(5000) or y > abs(5000):
            c = c + 1

print("wewnątrz:", a , "na bokach:", b ,"na zewnątrz:", c)