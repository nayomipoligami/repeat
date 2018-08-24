"""


Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)



"""
import time
print("""

MUKEMMEL SAYİ BULMA PROGRAMI

Çıkış için lutfen q'ya basin.....



""")

i=1
toplam=0
while 1:
    islem=input("lutfen yapmak istediginiz islemi seciniz e/q...:")
    if islem=="q":
        print("Programdan cikis yapiliyor....")
        break
    elif islem=="e":
        print("programa giris yapildi baslatiliyor..")
        time.sleep(1)
        sayi=int(input("Kontrol etmek istediginiz sayiyi girin..."))
        if sayi<0:
            print("lutfen pozitif sayi girin...")
            continue
        else:

            while i<sayi:
                if sayi%i==0:
                    toplam+=i
                i+=1
            if sayi == toplam:
                print("{} sayisi mukemmel bir sayidir.....".format(sayi))
            else:
                print("{} sayisi mukemmel bir sayi degildir.......".format(sayi))