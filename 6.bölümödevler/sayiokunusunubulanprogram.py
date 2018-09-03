"""

Problem 4
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi


"""
print("""


SAYİ OKUNUSU PROGRAMINA HOSGELDİNİZ....


""")


sayilar = {"sıfır":0,"bir":1,"iki":2,"üç":3,"dört":4,"bes":5,"altı":6,"yedi":7,"sekiz":8,"dokuz":9}
sayilar2={"on":10,"yirmi":20,"otuz":30,"kırk":40,"elli":50,"altmıs":60,"yetmıs":70,"seksen":80,"doksan":90}
def sayiokunusu_bulma():
    sayi=input("sayiyi girin.......:")
    liste=list()
    liste2=list()
    liste3=list()
    liste4=list()
    if len(sayi)<2:
        print("lutfen 2 basamakli sayi girin....")

    else:
        for i in sayi:
            i=int(i)
            liste.append(i)
        print(liste)
    for t in liste:
        for u,key in sayilar.items():
            if t==key:
                liste2.append(u)

    for y in liste:
        print(y,end="")
        liste4.append(y)

    print(liste4)



"""

# yazdırma okunusu
    for i in liste2:
        # print(i,end="")
        #y =keys
        # key1=values
        for y, key1 in sayilar2.items():
            if liste2[0] in sayilar.keys():
                liste2[0]=y
                print(liste2[0])

"""




sayiokunusu_bulma()






