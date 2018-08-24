import time
print("""

Carpim Tablosu Programına hosgeldiniz...

cıkmak icin lutfen q'ya basinnn....



""")


while True:
    islem=input("devam etmek icin e'ye cıkıs icin q'ya basın... e/q.....:")
    sayi1=int(input("ilk sayiyi girin:"))
    sayi2=int(input("ikinci sayiyi girin:"))

    if islem=="q":
        print("programimizi kullandiginiz icin tesekkurler programdan cikis yapiliyor...")
        time.sleep(1)
        break
    elif islem=="e":
        print("Programimiza tekrardan hosgeldiniz...")
        for i in range(sayi1,sayi2):
            print("********* {}. kademe****** ".format(i))
            for j in range(sayi1,sayi2):
                print("{}           {} * {} ={}                {}".format("*",i,j,i*j,"*"))





