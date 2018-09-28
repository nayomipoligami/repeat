import random

print("""

*********************************
Sayi Tahmini Oyununa Hosgeldiniz......
*********************************

""")
sayi=random.randint(1,100)
tahminhakki=5
isim=input("lutfen isminizi giriniz...:")
cinsiyet=input("cinsiyet girin ----- erkek \ bayan?:")
secenek=input("giris yapmak icin g ye cikis yapmak icin q ya basin...")

while 1:

    if secenek=="g":
        print("programa hosgeldiniz...")
        tahmin=int(input("tahmin ettiginiz sayiyi girin:"))

        if tahmin==sayi:
            print("tahmininiz dogru tebrikler....")
            if cinsiyet == "erkek":
                print("programimizi kullandıgınız icin tesekkurler {} bey..".format(isim))
                break
            else:
                print("programimizi kullandıgınız icin tesekkurler {} hanım..".format(isim))
                break
        elif tahmin>sayi:
            print("**********daha kucuk bir sayiyi girin***********...")
            tahminhakki-=1

        elif  tahmin<sayi:
            print("***************daha buyuk bir sayiyi girin**************...")
            tahminhakki-=1

        elif tahminhakki==0:
            print("tahmin hakkiniz bitti...")
    elif secenek=="q":
        if cinsiyet=="erkek":

            print("programimizi kullandıgınız icin tesekkurler {} bey..".format(isim))
            break
        else:

            print("programimizi kullandıgınız icin tesekkurler {} hanım..".format(isim))
            break