"""


Problem 2
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.


"""
print("""


EBOB BULMA PROGRAMINA HOSGELDİNİZ...



""")

def ebob():
    liste=list()
    liste2=list()
    ayni=list()
    a=int(input("sayi girin:"))
    b=int(input("sayi girin:"))
    maximum=0
    if a==0 or b==0:
        return 0
    else:
        for i in range(1,a+1):
            if a%i==0:
               liste.append(i)
            else:
                  continue
        for j in range(1,b+1):
            if b%j==0:
                liste2.append(j)
            else:
                continue
        for t in liste:
            for k in liste2:
                if t == k:
                    ayni.append(k)
        print("ortak bolenlerin listesi:", ayni)
        #print(max(ayni),"ebobdur...") kolay yolu bu ebobun ama algoritmasını bulucam.
        for u in ayni:
            if u>maximum:
                maximum=u
        print(maximum,"ebobdur.....")


ebob()





























































