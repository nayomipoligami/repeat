
import time
print("""
************************

FİBONACCİ SERİSİ PROGRAMI

************************

Çıkıs için lutfen q'ya basiniz....



""")
#1,2,3,5,8,13,21,34.....


print("Program baslatiliyor...")
time.sleep(1)
a=1
b=2
liste=[1,2]
while 1:
    islem=input("lutfen yapmak istediginiz islemi seciniz 1/q ya basin....")
    if islem=="q":
        print("Programdan cikis yapiliyor...")
        break
    elif islem=="1":
        print("fibonacci serisi bulma programina hosgeldiniz...")
        sayi=int(input("kaca kadar Fibonacci serisi bulmak isttiyorsunuz?:"))
        if sayi<0:
            print("lutfen pozitif bir sayi giriniz...")
            continue
        else:
            for i in range(a,sayi):
                a,b=b,a+b
                liste.append(b)
                print(liste,"<--- {}.adim".format(i))

