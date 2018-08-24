print(""""

*******************

tam sayi bölenlerini bulma programı

programin kac saniyede sonladngınıda buluyor....

*******************
""")
import time
start_time = time.time()
def tambolenbulma(sayi):
        liste = list()
        i=0
        for i in range (1,(sayi//2)+1):
            if sayi%i==0:
                liste.append(i)

            else:
                continue
        liste.append(sayi)
        print("tam bolenlerin listesi",liste)
        print(len(liste))

while 1:
        sayi=input("giris yapin:")
        if sayi=="q":
            break
        else:
            sayi=int(sayi)
            tambolenbulma(sayi)
print("--- %s seconds ---" % (time.time() - start_time))
