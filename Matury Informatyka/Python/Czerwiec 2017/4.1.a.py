a = []

for i in range(2, 10001):
    for j in range(2, 10001):
        if i == j:
            a.append(i)
            break
        if i % j == 0:
            break

print(a)

            
            
