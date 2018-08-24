print ("GİRİLEN SAYININ TÜRKÇE OKUNUŞUNU VEREN PROGRAMA HOŞGELDİNİZ\n\nBu program en fazla 12 basamaklı sayıları okuyabilmektedir.")
söz1 = {1:"Bir",2:"İki",3:"Üç",4:"Dört",5:"Beş",6:"Altı",7:"Yedi",8:"Sekiz",9:"Dokuz"}
söz2 = {1:"On",2:"Yirmi",3:"Otuz",4:"Kırk",5:"Elli",6:"Altmış",7:"Yetmiş",8:"Seksen",9:"Doksan"}
söz3 = {2:"İki",3:"Üç",4:"Dört",5:"Beş",6:"Altı",7:"Yedi",8:"Sekiz",9:"Dokuz"}
def oku3 (s,b = False):
    if len (s) == 0:
        return ""
    elif len (s) == 1:
        if b and s == "1":
            return ""
        return söz1.get(int(s))
    elif len (s) == 2:
        if s[1] == "0":
            return söz2.get(int(s[0]))
        else:
            return söz2.get(int(s[0]))+" "+söz1.get(int(s[1]))
    else:
        if s[0] == "0":
            if s[1] == "0":
                if (b and s[2] == "1") or s[2] == "0":
                    return ""
                else:
                    return söz1.get(int(s[2]))
            else:
                if s[2] == "0":
                    return söz2.get(int(s[1]))
                else:
                    return söz2.get(int(s[1]))+" "+söz1.get(int(s[2]))
        elif s[1] == "0":
            if s[2] == "0":
                if s[0] == "1":
                    return "Yüz"
                else:
                    return söz3.get(int(s[0]))+" Yüz"
            else:
                if s[0] == "1":
                    return "Yüz "+söz1.get(int(s[2]))
                else:
                    return söz3.get(int(s[0]))+" Yüz "+söz1.get(int(s[2]))
        else:
            if s[2] == "0":
                if s[0] == "1":
                    return "Yüz "+söz2.get(int(s[1]))
                else:
                    return söz3.get(int(s[0]))+" Yüz "+söz2.get(int(s[1]))
            else:
                if s[0] == "1":
                    return "Yüz "+söz2.get(int(s[1]))+" "+söz1.get(int(s[2]))
                else:
                    return söz3.get(int(s[0]))+" Yüz "+söz2.get(int(s[1]))+" "+söz1.get(int(s[2]))
def okuma (s):
    if s == 0:
        return "Sıfır"
    o = ""
    if abs(s) != s:
        o += "Eksi"
        s = abs(s)
    y = str (s)
    u = len (y)
    x2 = ""
    x3 = ""
    x4 = ""
    if u <= 3:
        x1 = y
    elif u <= 6:
        x1 = y[-3:]
        x2 = y[:-3]
    elif u <= 9:
        x1 = y[-3:]
        x2 = y[-6:-3]
        x3 = y[:-6]
    else:
        x1 = y[-3:]
        x2 = y[-6:-3]
        x3 = y[-9:-6]
        x4 = y[:-9]
    b = False
    if (len(x2) == 0) or (x2 == "000"):
        ek1 = ""
    else:
        if (x2 == "1") or (x2 == "001"):
            b = True
        ek1 = "Bin"
    if (len(x3) == 0) or (x3 == "000"):
        ek2 = ""
    else:
        ek2 = "Milyon"
    if (len(x4) == 0):
        ek3 = ""
    else:
        ek3 = "Milyar"
    l=[oku3(x4),ek3,oku3(x3),ek2,oku3(x2,b),ek1,oku3(x1)]
    for i in l:
        if (len(i) != 0):
            if (len(o) == 0):
                o += i
            else:
                o += " "+i
    return o
while True:
    s = int (input ("\nLütfen herhangi bir tamsayı giriniz:"))
    if len(str(abs(s))) > 12:
        print (s,"12'den fazla basamağa sahip.")
        continue
    print("\n",s," ---> ",okuma (s),"\n",sep="")
    while True:
        k = input ("Programda kalmak istiyor musunuz?(E/H):")
        if k == "E" or k == "H":
            break
        else:
            print ("Geçerli bir komut girin.")
    if k == "E":
        continue
    break