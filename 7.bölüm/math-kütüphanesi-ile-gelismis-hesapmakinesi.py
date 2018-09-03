import math
import time


"""

Proje 1
Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.

"""
print(
    """
    
    Gelişmiş Hesap Makinesine Hosgeldiniz...
         İŞLEMLER:
                1 = toplama
                2 = cikarma
                3 = carpma
                4 = bölme
                5 = sayının faktoriyelini bulma 
                6 = sayının sinüsünü bulma
                7 = sayının cosinüsünü bulma
                8 = sayının tanjantını bulma 
                9 = sayının cotanjantını bulma 
                10 = sayının logaritma (10) tabanında eşiti
                11 = sayinin karekökü 
                 cikis icin lutfen q ya basin....
    """
)
def hesapmakine():
    while 1:
        secim=input("yapmak istediginiz secimi :")

        if secim=="1":
            sayi1=int(input("lutfen ilk sayiyi girin:"))
            sayi2=int(input("lutfen ikinci sayiyi girin:"))
            print("sayilariniz toplaniyor lutfen bekleyin......")
            time.sleep(1)
            toplam=sayi1+sayi2
            print("toplam= {}".format(toplam))
            continue
        elif secim=="2":
            sayi1 = int(input("lutfen ilk sayiyi girin:"))
            sayi2 = int(input("lutfen ikinci sayiyi girin:"))
            if sayi1>=sayi2:
                sonuc=sayi1-sayi2
                print("cikarma islemi yapiliyor lutfen bekleyin....")
                time.sleep(1)
                print("cikarma isleminin sonucu ={}".format(sonuc))
            else:
                sonuc=sayi2-sayi1
                print("cikarma islemi yapiliyor lutfen bekleyin....")
                time.sleep(1)
                print("cikarma isleminin sonucu ={}".format(sonuc))
            continue
        elif secim=="3":
            sayi1 = int(input("lutfen ilk sayiyi girin:"))
            sayi2 = int(input("lutfen ikinci sayiyi girin:"))
            print("sayilariniz carpiliyor lutfen bekleyin......")
            time.sleep(1)
            carpma = sayi1 * sayi2
            print(" carpma= {}".format(carpma))
            continue
        elif secim=="4":
            sayi1 = float(input("lutfen ilk sayiyi girin:"))
            sayi2 = float(input("lutfen ikinci sayiyi girin:"))
            if sayi1 >= sayi2:
                bölme = sayi1 / sayi2
                print("bölme islemi yapiliyor lutfen bekleyin....")
                time.sleep(1)
                print("bölme isleminin sonucu ={}".format(round(bölme,2)))
            else:
                bölme = sayi2 / sayi1
                print("bölme islemi yapiliyor lutfen bekleyin....")
                time.sleep(1)
                print("bölme isleminin sonucu ={}".format(round(bölme,2)))
            continue
        elif secim=="5":
            sayi1 = int(input("factoriali alinacak  sayiyi girin:"))
            fact=math.factorial(sayi1)
            print("factorial islemi yapiliyor lutfen bekleyin....")
            time.sleep(1)
            print("factorial isleminin sonucu ={}".format(fact))
        elif secim=="6":
            sayi1 = int(input("sinusu bulunacak sayiyi girin:"))
            sinus=math.sin(sayi1)
            print("sinus bulma islemi yapiliyor lutfen bekleyin....")
            time.sleep(1)
            print("sayinin sinusu  ={}".format(sinus))
        elif secim=="7":
            sayi1 = int(input("cosinusu bulunacak sayiyi girin:"))
            cosinus = math.cos(sayi1)
            print("cosinus bulma islemi yapiliyor lutfen bekleyin....")
            time.sleep(1)
            print("sayinin cosinusu  ={}".format(cosinus))
        elif secim=="8":
            sayi1 = int(input("cosinusu bulunacak sayiyi girin:"))
            tanjant = math.tan(math.radians(sayi1))
            print("tanjanti bulma islemi yapiliyor lutfen bekleyin....")
            time.sleep(1)
            print("sayinin tanjanti  ={}".format(tanjant))
        elif secim=="9":
            sayi1 = int(input("cotanjantı bulunacak sayiyi girin:"))
            cotanjant = 1/ (math.tan(math.radians(sayi1)))
            print("cotanjantı bulma islemi yapiliyor lutfen bekleyin....")
            time.sleep(1)
            print("sayinin cotanjantı  ={}".format(cotanjant))
        elif secim=="10":
            sayi1 = int(input("logaritmasi bulunacak sayiyi girin:"))
            logaritma = math.log10(sayi1)
            print("logaritma bulma islemi yapiliyor lutfen bekleyin....")
            time.sleep(1)
            print("sayinin logaritma  ={}".format(logaritma))
        elif secim == "11":
            sayi1 = int(input("karekökü bulunacak sayiyi girin:"))
            karekök = math.sqrt(sayi1)
            print("karekökü bulma islemi yapiliyor lutfen bekleyin....")
            time.sleep(1)
            print("sayinin kaekökü  ={}".format(float(round(karekök,2))))

        elif secim=="q":
            print("programimizi kullandiginiz icin tesekkurler programdan cikis yapiliyor....")
            time.sleep(2)
            break
        else:
            print("ust menuye donus yapiliyor ...")
            input("enter a basinnn")


hesapmakine()