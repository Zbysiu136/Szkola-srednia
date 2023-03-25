def Cyferki(n, A):
    if A[-2] % 2 == 1:
        return A[-1]

    r = n - int(n/2)

    for i in range(0, n-1):
        if A[r] % 2 == 1:
            r = n - int(r/2)
        
        if A[r] % 2 == 0:
            for j in range(r, 0, -1):
                if A[j] % 2 == 1:
                    return A[j+1]


print(Cyferki(10, [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]))

#złoźoność logarytmiczna

        


