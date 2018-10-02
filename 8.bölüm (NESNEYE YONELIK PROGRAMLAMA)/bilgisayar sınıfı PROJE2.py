import time
import datetime

an = datetime.datetime.now()#datetime sınıfından an nesnesini olusturduk..

class Bilgisayar ():
    def __init__(self,bilgisayar_durum="kapali",ram=[4],ekran_karti=["gtx 1050"],islemci="i7",monitor="lenovo",programlar=list(),bilgisayar_Ses=0,bilgisayar_parlaklik=0,saatim=an.hour):


        self.bilgisayar_durum=bilgisayar_durum
        self.ram=ram
        self.ekran_karti=ekran_karti
        self.islemci=islemci
        self.monitor=monitor
        self.programlar=programlar
        self.bilgisayar_Ses=bilgisayar_Ses
        self.bilgisayar_parlaklik=bilgisayar_parlaklik


    def __str__(self):
    # print bilgisayar  nesnesi yazdıgımızda bize bu fonksiyonu dondursun dıye bu print fonk yerine gecicek..
        return "bilgisayardurum : {}\nRam :{}\nEkranKarti :{}\nİslemci :{}\nMonitor :{}\n".format(self.bilgisayar_durum,self.ram,self.ekran_karti,self.islemci,self.monitor)


    def __len__(self):
        return len(self.ekran_karti)


    def __del__(self):
        print("bilgisayar nesnesi siliniyor..")
        time.sleep(1)
        print("silindi....")


    def acik_Duruma_getir(self):

        if self.bilgisayar_durum=="kapali":
            self.bilgisayar_durum="acik"
            print("bilgisayar aciliyor..")
            time.sleep(1)
        else:
            print("bilgisayar zaten acik...")


    def Kapali_Duruma_getir(self):

        if self.bilgisayar_durum=="kapali":
            print("bilgisayariniz zaten kapali..")

        else:
            self.bilgisayar_durum="acik"
            print("bilgisayariniz kapatiliyor..")
            time.sleep(1)


    def program_ekle(self,eklenecek):
        eklenecek=input("eklenecek programı giriniz.(eğer birden fazla program girecekseniz  ',' ile girin")
        eklenecek=eklenecek.split(",")
        for eklenecek in self.programlar:
            for i in self.programlar:
                if i!=eklenecek:
                    self.programlar.append(eklenecek)
                else:
                    print("ayni program zaten var...")


    def saat_degistirme(self):
        # ornek olarak eger saat 1 ise saati 1 azalttıgımızda 12 olmalı! bu onemlı!
        while True:

            oynama = input("saati artırmak icin ' + ' azaltmak icin ' - ' ye cikis icin 'q' ye basin: ")
            if oynama == "+":
                if self.saatim >= 12:
                    pass
                else:
                    self.saatim += 1
                    print("saat ayarı yapildi güncel saat:{}".format(self.saatim))
            elif oynama == "-":
                if self.saatim > 1:
                    self.saatim -= 1
                    print("saat ayarı yapildi güncel saat:{}".format(self.saatim))
                elif self.saatim == 1:
                    self.saatim = 12
                    print("saat ayarı yapildi güncel saat:{}".format(self.saatim))
                elif self.saatim == 0:
                    self.saatim = 11
                elif oynama == "Q" or oynama == "q":
                    break
                else:
                    pass
            else:
                print("hatalı giris")
                break


    def saat_degistirme(self):
        # ornek olarak eger saat 1 ise saati 1 azalttıgımızda 12 olmalı! bu onemlı!
        while True:

            oynama = input("saati artırmak icin ' + ' azaltmak icin ' - ' ye cikis icin 'q' ye basin: ")
            if oynama == "+":
                if self.saatim >= 12:
                    pass
                else:
                    self.saatim += 1
                    print("saat ayarı yapildi güncel saat:{}".format(self.saatim))
            elif oynama == "-":
                if self.saatim > 1:
                    self.saatim -= 1
                    print("saat ayarı yapildi güncel saat:{}".format(self.saatim))
                elif self.saatim == 1:
                    self.saatim = 12
                    print("saat ayarı yapildi güncel saat:{}".format(self.saatim))
                elif self.saatim == 0:
                    self.saatim = 11
                elif oynama == "Q" or oynama == "q":
                    break
                else:
                    pass
            else:
                print("hatalı giris")
                break



print("""

        BİLGİSAYAR UYGULAMASI

        1. PC ac

        2. PC kapat

        3. Ses Ayarları

        4. Program Ekle

        5. Bilgisayar bilgileri

        6. Saat Ayarlama

        Cikis icin "q" ya basin...



""")