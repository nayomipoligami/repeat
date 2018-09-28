import random
import time
import os

print("""

********************************

sayi tahmin etme oyununa hosgeldiniz....

********************************


""")
randomsayi=random.randint(1,40)
tahmin=7
while 1:

    bizimsayimiz=int(input("lutfen tahmininizi girin:"))

    if bizimsayimiz==randomsayi:
        print("Tahmininiz sorgulanıyor lutfen bekleyin....")
        time.sleep(2)
        print("Tebrikler tahmininiz dogru ! sayi:",bizimsayimiz)

        break
    elif bizimsayimiz<randomsayi:
        print("Tahmininiz sorgulanıyor lutfen bekleyin....")
        time.sleep(2)
        print("lutfen daha buyuk bir sayi girin")
        tahmin-=1
        if tahmin == 0:
            print("tahmin hakkiniz bitti programdan cikis yapiliyor....")
            time.sleep(1)
            break
    else:
        print("Tahmininiz sorgulanıyor lutfen bekleyin....")
        time.sleep(2)
        print("lutfen daha kucuk bir sayi girin")
        tahmin -= 1
        if tahmin==0:
            print("tahmin hakkiniz bitti programdan cikis yapiliyor....")
            time.sleep(1)
            break
