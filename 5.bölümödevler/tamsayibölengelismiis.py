print("""
************************


İstenilen aralıkta istenilen tam sayiya tam bölen bulma 
Programına Hosgeldiniz...



************************


""")

"""

21-31 2 ile bölünme



"""
import time
liste3=list()
while 1:

    islem = input("isleme devam etmek istiyormusunuz ? e/h    :")

    if islem=="e":
        sayi1 = int(input("ilk sayiyi girin      :"))
        sayi2 = int(input("aralıgı belirleyecek 2. sayiyi girin    :"))
        bölen = int(input("hangi sayiya tam böleni bulmak istiyorsunuz?     :"))
        if sayi1<sayi2:
            for i in range(sayi1, sayi2+1):
                   if i%bölen==0:
                       liste3.append(i)
            print("Tam bölünen elemanlarin listesi=", liste3)
            continue
        elif sayi2>sayi1:
            for i in range(sayi2, sayi1 + 1):
                if i % bölen == 0:
                    liste3.append(i)
            print("Tam bölünen elemanlarin listesi=", liste3)
            continue
        elif sayi1==sayi2:
            if bölen==sayi1 or bölen==sayi2:
                liste3.append(bölen)
                print("Tam bölünen elemanlarin listesi=", liste3)
            else:
                print("liste boş")
    elif islem=="h":
        print("Programimizi kullandiginiz icin tesekkurler programdan cikis yapiliyor...")
        time.sleep(2)
        break
