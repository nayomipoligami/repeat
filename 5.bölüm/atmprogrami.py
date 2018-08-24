import time
import math
print("""
***********************************

Atm Makinesi Programina hosgeldiniz....



1.Bakiye Sorgulama
2.Para Yatırma
3.Para Çekme
4.Para Gönderme
5 - Borç Ödeme/Sorgulama

Programimizdan cikmak icin q'ya basiniz...


***********************************
""")
sys_parola = "12345"
giris_hakki = 3
bakiye=0
while True:
    parola = input("hoşgeldiniz,lütfen parolanızı giriniz: ")

    if (parola == sys_parola):
            print("giris yapildi...")
            while True:
                islem = (input("lutfen yapmak istediginiz islemi seciniz...:(cikis icin q'ya basin..) "))
                if islem=="q":
                    print("programimizdan cikiliyor...lutfen bekleyin")
                    time.sleep(1)
                    print("cikis yapildi.....")
                    break
                elif islem=="1":
                    print("bakiyeniz ={}".format(bakiye))
                    print("baska islem yapmak istiyormusunuz e/h ?:")
                    secenek=input("e/h ?:")
                    if secenek=="e":
                        continue
                    else:
                        break
                elif islem=="2":
                    print("para yatirma isleminiz baslatiliyor..")
                    time.sleep(1)
                    yatirilcak_miktar=int(input("yatirilcak miktari girin :"))
                    onay=input("e/h ?:")
                    if onay=="e":
                        bakiye+=abs(yatirilcak_miktar)
                        print("paraniz yatiriliyor lutfen bekleyiniz")
                        print("yeni bakiyeniz:{}".format(bakiye))
                    else:
                        print("baska islem yapmak istiyormusunuz e/h ?:")
                        secenek = input("e/h ?:")
                        if secenek == "e":
                            continue
                        else:
                            break
                elif islem == "3":
                    print("para cekme isleminiz baslatiliyor..")
                    time.sleep(1)
                    cekilen_miktar = int(input("cekilecek miktari girin :"))
                    if bakiye - cekilen_miktar<0:
                        print("para cekiminiz basarisiz ....")
                        continue
                    else:
                        onay = input("e/h ?:")
                        if onay == "e":
                            bakiye -= abs(cekilen_miktar)
                            print("paraniz cekiliyor lutfen bekleyiniz...")
                            print("yeni bakiyeniz:{}".format(bakiye))
                        else:
                            print("baska islem yapmak istiyormusunuz e/h ?:")
                            secenek = input("e/h ?:")
                            if secenek == "e":
                                continue
                            else:
                                break
                elif islem=="4":
                    havale_no=int(input("lutfen havale gönderilcek numarayi girin:"))
                    print("hesabına para yatırılcak numara{}".format(havale_no))
                    gonderilen_para=int(input("gonderilcek miktari girin...:"))
                    onay = input("e/h ?:")
                    if onay == "e":
                        bakiye -= abs(gonderilen_para)
                        print("paraniz gonderiliyor lutfen bekleyiniz...")
                        print("yeni bakiyeniz:{}".format(bakiye))
                    else:
                        print("baska islem yapmak istiyormusunuz e/h ?:")
                        secenek = input("e/h ?:")
                        if secenek == "e":
                            continue
                        else:
                            break
                elif islem=="5":
                    ödeme_secenekleri=input("karttanödeme(1)/ parayatırma(2) /ustmenuyedonus(3):")
                    if ödeme_secenekleri=="1":
                        print("kart bakiyeniz",bakiye)

                        ödeme_miktari=int(input("ödenecek miktari girin:"))
                        onay = input("e/h ?:")
                        if bakiye-ödeme_miktari<0:
                            print("bakiyeniz yetersiz... ")
                        else:
                            if onay == "e":
                                bakiye -= abs(ödeme_miktari)
                                print("paraniz ödeniyor lutfen bekleyiniz...")
                                print("yeni bakiyeniz:{}".format(bakiye))
                            else:
                                print("baska islem yapmak istiyormusunuz e/h ?:")
                                secenek = input("e/h ?:")
                                if secenek == "e":
                                    continue
                                else:
                                    break
                    elif ödeme_secenekleri=="2":
                        borcödeme_nakit=int(input("nakit nekadar ödüyceğinizi girin:"))
                        print("ödenecek miktar",borcödeme_nakit)
                        if onay == "e":
                            print("paraniz ödeniyor lutfen bekleyiniz...")
                        else:
                            print("baska islem yapmak istiyormusunuz e/h ?:")
                            secenek = input("e/h ?:")
                            if secenek == "e":
                                continue
                            else:
                                break
                    elif ödeme_secenekleri=="3":
                        continue
                else:
                    print("lutfen 1/2/3/4 seceneklerinden birine basin...")
                    continue
    else:
        giris_hakki-=1
        print("parolaniz yanlis lutfen tekrar deneyin...")
        if(giris_hakki==0):
            print("giris hakkiniz bitti lutfen bankanızı arayınız...")
            break