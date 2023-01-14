with open(r"C:\Users\zbysi\Desktop\Informatyka\Python\Czerwiec 2021\napisy.txt") as f:
    str = ""


    for i in f:
        x = list(i)
        x.pop()

        ok = 0
        para = ""

        for j in x:

            if j == "0" or j == "1" or j == "2" or j == "3" or j == "4" or j == "5" or j == "6" or j == "7" or j == "8" or j == "9":
                ok = ok + 1
                para = para + j


                if ok == 2 and int(para)>=65 and int(para)<=90:
                    str = str + chr(int(para))
                    ok = 0
                    para = ""

                    if str[-1] == "X" and str[-2] == "X" and str[-3] == "X":
                        print(str)

