

def armstrong_hesabi ():
    sayi = (input("lutfen sayi girin:"))
    temp=0
    basamak = len(sayi)
    print("basamak sayisi :",basamak)
    sayi=int(sayi)
    toplama=0
    i=1
    for i in range(i,sayi+1):
        temp=sayi%10
        toplama+=temp**basamak
        i*=10
    if toplama==sayi:
            print("{} sayisi armstrong bir sayidir......".format(sayi))

    else:
            print("{} sayisi armstrong degildir.....".format(sayi))
armstrong_hesabi()
