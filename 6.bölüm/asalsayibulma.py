def asalsayi_Bulma(a):
    if a==1:
        return False
    elif a==2:
        return True
    else:
        for i in range(2,a):
            if a%i==0:
                return False
            else:
                return True
while 1:
    a=input("girin:")
    if a=="q":
        break
    else:
        a=int(a)
        if asalsayi_Bulma(a):#yani buraya girmesi demek asalmi fonksiyonuna girmis true deger döndurmus demek
            print(a,"sayisi asaldir..")
        else:#bu asalmi fonksiyonuna girmemis demekk
            print("sayi asal degildir....")












