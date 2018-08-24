"""
Problem 3
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

"""

print("""

EKOK BULMA PROGRAMINA HOSGELDİNİZ....



""")

def ekok():
    liste=list()
    liste2=list()
    a = int(input("sayi girin:"))
    b = int(input("sayi girin:"))
    ayni=list()
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
        for u in ayni:
            if u>maximum:
                maximum=u
    ekok=a*b/maximum
    print(ekok,"ekoktur")


ekok()