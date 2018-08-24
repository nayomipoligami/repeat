
"""
sözlük={"bir":1,"iki":2,"ondört":14,"yirmialtı":26}
print(sözlük)
sözlük2 = {"üç":3,"beş":5,"iki":2,"bir":1,"altı":6,"yirmi":20}
print(sözlük2)
for i in sözlük.values():
    print(i)
print("*****************\n")

for i in sözlük2.values():
    print(i)

"""
""" 

liste_Tek=[]
liste_Cift=[]
for i in range(1,11):
    sayi=int(input("lutfen listelencek sayilari giriniz:"))
    if sayi%2==0:
        liste_Cift.append(sayi)
    else:
        liste_Tek.append(sayi)
print("tek sayilar ={}".format(liste_Tek))
print("cift sayilar ={}".format(liste_Cift))




"""

""" 
liste = []
listeçift = []
listetek = []
sayı = int(input("Kaç Tane Sayı Gireceksin?: "))
for sıra in range(1, sayı + 1):
    liste.append(int(input(str(sıra) + ". Sayıyı Giriniz: ")))

for eleman in liste:
    if (eleman % 2 == 0):
        listeçift.append(eleman)
    else:
        listetek.append(eleman)
print("Çift Sayılar:", listeçift)
print("Tek Sayılar:", listetek)





"""
"""
#LİSTEDEKİ HER ELEMANI 1 ARTIRIP TOPLAMI HESAPLAMAK!
pasta=[1,2,3,4,5,6,7]
toplam=0
for i in pasta:
    i+=1
    print("yeni elemanlar ={}".format(i))
    toplam+=i
    print(toplam)
print("en sonki toplam={}".format(toplam))



"""

#böyle bir durumda 2. indexler yerine sadece 0 ve 1 leri istemem nasıl mümkün olur?
#BU SORUNU ÇÖZZZZ....



liste=[(2,34,5),(2,23,4),('w',2,3)]


for (a,b) in liste:
     print(a,b)





