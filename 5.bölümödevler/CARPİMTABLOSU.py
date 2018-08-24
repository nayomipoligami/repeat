"""

Problem 3
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.

"""
import time
print("""

Carpim Tablosu Programına hosgeldiniz...

cıkmak icin lutfen q'ya basinnn....



""")


while True:
    islem=input("devam etmek icin e'ye cıkıs icin q'ya basın... e/q.....:")
    if islem=="q":
        print("programimizi kullandiginiz icin tesekkurler programdan cikis yapiliyor...")
        time.sleep(1)
        break
    elif islem=="e":
        print("Programimiza tekrardan hosgeldiniz...")
        for i in range(1,11):
            print("********* {}. kademe bitti************".format(i-1))
            for j in range(1,11):
                print("{}           {} * {} ={}              {}".format("*", i, j, i * j,"*"))





