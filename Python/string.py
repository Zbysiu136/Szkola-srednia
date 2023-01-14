txt  = "ananas"
txt2 = "afsafkja0jwijfiojgkohnjoehs"
zmienna = 0 


#własności print
print("ana",zmienna,"nas") #ana 0 nas
print("ana", zmienna ,"nas") #ana 0 nas
print("ana" + "nas") #ananas
print("ana", "nas") #ana nas


#długość ciągu znaków
print("długość ciągu",len(txt))

#wyświetlanie określonych miejsc ciągu, od 0 bez ostaniego - nan
print("znaki od 1 do 3",txt[1:4])


#działanie na string
print(txt.lower()) #ananas
print(txt.upper()) #ANANAS
print(txt.swapcase()) #AnAnAs = aNaNaS
print(txt.split(" ")) #Dzielenie tekstu na elementy tablicy w momentach argumentu

#usunięcie znaków z lewej i prawej
print(txt2.strip("a"))

#zamienia literki a na h w całym ciągu
print(txt.replace("a", "h")) #hnhnhs

#przecina ciąg znaków w częśc podczas określonego argumentu pomijając go
print(txt.split("a")) # ['', 'n', 'n', 's']

#dodawanie wartości int do string
zamowienie = "Masz {0} monet"
print(zamowienie.format(zmienna)) 


#ile razy wystąpił dany znak
print("a wystąpiło",txt.count("a"),"razy")

print(txt.find("n")) #pozycja znaku n w ciągu, zwróci -1 gdy nie znajdzie

print(txt2.isdigit()) #true jeżeli cały ciąg jest cyfrowy
print(txt2.isalpha()) #true jeżeli cały ciąg jest a-z



# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value