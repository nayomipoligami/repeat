"""

Problem 4
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.
Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.



"""

print("""

Uygulamamiza Hosgeldiniz...

Cikis icin lutfen q' ya basin....

""")
toplam=0
while 1:

    sayi=(input("sayi girisi yapin  veya cikis yapin (cikis icin q'ya basin...):"))
    if sayi =="q":
        print("programdan cikis yapiliyor....")
        break
    toplam+=int(sayi)

print("toplam",toplam)




























