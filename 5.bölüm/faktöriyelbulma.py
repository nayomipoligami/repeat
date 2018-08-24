print("""
**************

FAKTÖRİYEL BULMA PROGRAMI

Çıkıs icin lutfen q'ya basin...


**************

""")
faktoriyel=1
while True:
    islem=input("lutfen yapmak istediginiz islemi girin 1/q:")
    if islem=="q":
        print("programdan cikis yapiliyor....")
        break
    elif islem=="1":
        sayi=int(input("lutfen faktöriyelini bulmak istediginiz sayiyi giriniz:"))
        if sayi<0:
            print("sayinin faktöriyeli bulunamaz")
        elif type(sayi)==float:
            print("lutfen int bir sayi girin...")
        else:
            for i in range(1,sayi+1):
                faktoriyel*=i
            print("faktöriyel ={}".format(faktoriyel))
            faktoriyel=1
            continue