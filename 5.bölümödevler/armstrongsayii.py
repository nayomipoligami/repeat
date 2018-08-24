"""

Problem 2
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan
herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4


"""
import math
import time
print("""

Armstrong Sayi Bulma Programi

Çıkıs için lutfen q'ya basin....




""")
i=1
kac_basamakli = 1
n=0
a=1
yeni=0
liste=[]
toplam=0
while True:
    islem=input("yapmak istediginiz islemi girin   (e/q)  :")
    if islem=="q":
        print("programdan cikis yapiliyor...")
        break
    elif islem=="e":
        print("Armstrong sayisi bulma programina hosgeldiniz...")
        sayi=int(input("hangi sayiyi kontrol etmek istiyorsunuz :  "))
        #basamak sayisi bulma
        while  i*10<=sayi :
            sayi/=10
            kac_basamakli+=1
        print("sayi {} basamaklidir...".format(kac_basamakli))
        time.sleep(1)
        onay=input("armstrong olup olmadıgını bulmak istiyormusunuz e/h:")
        if onay=="e":
            print("armstrong olup olmadıgı bulunuyor....")

            for i in str(sayi):
                rakam = int(i) ** kac_basamakli
                toplam += rakam
                if (sayi == toplam):
                    print("Bu Bir Armstrong Sayısıdır.")
                else:
                    print("Armstong Sayısı Degildir.")
        else:
            print("hicbir sey yapilmadi...")
        kac_basamakli = 1
        continue