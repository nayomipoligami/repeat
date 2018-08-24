def bolenler():
    liste=list()
    toplam=0
    a=int(input("sayi girin:"))
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        for i in range(1,a+1):
            if a%i==0:
               liste.append(i)
               toplam+=i
            else:
                  continue
        if toplam==a:
            print(a,"sayisi mukemmel bir sayidir...")
        else:
            print(a,"sayisi mukemmel bir sayi degildir...")
        print(liste)
bolenler()


