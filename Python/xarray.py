txt = ["ananas", "arbuz", "pomidor"]
num = [3,6,2,1,22,21,4,2,5]
tri = []
słownik = {}
słownik[słowo] = definicja #dla takiego samego słowa poprzednia definicja zostanie zastąpiona nową

txt.append("ogórek") #dodaje warość na koneic tablicy
txt.insert(1, "banan") #dodaje zawartość na określonej pozycji
tri.clear() #czyści całą tablice

txt.pop(3) #usuwa element na określonej pozycji
num.remove(21) #usuwa określoną wartość z tablicy
txt.reverse() #odwraca kolejnośc tablicy

set(num) #usuwa duplikaty z tablicy



tri.extend(txt) #łączy zawartość dwóch tablic
print(num.count(2)) #ilość wystąpień podanego argumentu w tablicy
print(num.index(1)) #pozycja argumentu w tablicy 

num.sort()
print(num)