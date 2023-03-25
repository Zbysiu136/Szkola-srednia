count = 0
I = []
J = []

with open(r'C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2018\dane1.txt') as f:
    for i in f:
        i = i.split(" ")
        i = i[-1]
        i = i[0:-1]

        I.append(i)




with open(r'C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2018\dane2.txt') as g:
    for j in g:

        j = j.split(" ")
        j = j[-1]
        j = j[0:-1]

        J.append(j)

for i in range(0, len(I)):
    print(I[i], J[i])
    if I[i] == J[i]:

        count = count + 1

print(I, J)
print(count)


