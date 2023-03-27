with open(r"C:\Users\zbysi\Desktop\Nowy folder\liczby.txt") as f:
    count = 0
    for i in f:
        
        
        for j in range(0, 99):
            if int(i) == pow(3, j):
                count = count + 1
                break
        
    
print(count)