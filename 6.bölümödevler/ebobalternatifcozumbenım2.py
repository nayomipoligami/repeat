def ebob(sayi, sayi2):
    ebob = 1
    i=1
    if sayi>sayi2:
        while i<sayi:
            if sayi%i==0 and sayi2%i==0:
                ebob=i
            i+=1
        return ebob
    elif sayi2>sayi:
        while i<sayi2:
            if sayi%i==0 and sayi2%i==0:
                ebob=i
            i+=1
        return ebob
    else:
        ebob=sayi
        return ebob
while 1:
    secim=input("giris icin e ye cikis icin q' ya basin.......:")
    if secim=="e":
        sayi=int(input("sayi:"))
        sayi2=int(input("sayi2:"))
        print("ebob :",ebob(sayi,sayi2))
    elif secim=="q":
        break
    else:
        print("yanlis secim yaptiniz lutfen dogru secim yapin ....")
        input("ana menuye donmek ıcın entera basın")
