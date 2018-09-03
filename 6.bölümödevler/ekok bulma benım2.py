def ekok():
        snc=1
        sayi1=int(input("sayi1:"))
        sayi2 = int(input("sayi2:"))
        for i in range(1,sayi1+1,sayi2+1):
            if sayi1%i ==0 and sayi2%i==0:
                snc*=i
            i+=1
        return print(snc)
ekok()

