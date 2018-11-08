import time
import datetime

an = datetime.datetime.now()#datetime sınıfından an nesnesini olusturduk..

class Bilgisayar ():
    def __init__(self,bilgisayar_durum="kapali",ram=[4],ekran_karti=["gtx 1050"],islemci="i7",monitor="lenovo",programlar=[],bilgisayar_Ses=0,bilgisayar_parlaklik=0,saatim=an.hour):

        self.bilgisayar_durum=bilgisayar_durum
        self.ram=ram
        self.ekran_karti=ekran_karti
        self.islemci=islemci
        self.monitor=monitor
        self.programlar=programlar
        self.bilgisayar_Ses=bilgisayar_Ses
        self.bilgisayar_parlaklik=bilgisayar_parlaklik
        self.saatim=saatim

    def __str__(self):
    # print bilgisayar  nesnesi yazdıgımızda bize bu fonksiyonu dondursun dıye bu print fonk yerine gecicek..
        return "bilgisayardurum : {}\nRam :{}\nEkranKarti :{}\nİslemci :{}\nMonitor :{}\nProgramlar : {}\nBilgisayarSes : {}\nBilgissayarParlaklik:{}\nSaatim :{}\n".format(self.bilgisayar_durum,self.ram,self.ekran_karti,self.islemci,self.monitor,self.programlar,self.bilgisayar_Ses,self.bilgisayar_parlaklik,self.saatim)


    def __len__(self):
        return len(self.ekran_karti)



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
            self.bilgisayar_durum="kapali"
            time.sleep(1)
            print("bilgisayar kapandi.")


    def program_ekle(self,program):
        print("program yukleniyor..")
        time.sleep(1)
        self.programlar.append(program)
        print("program basriyla yuklendi...")




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
    def ses_Ayarları(self):
        while True:
            cevap = input("sesi azalt :'< '\n sesi arttır '>'\n cikis : 'cikis' ")

            if cevap == "<":
                if self.bilgisayar_Ses != 0:

                    print("ses azaltılıyor...")
                    self.bilgisayar_Ses -= 1
                    print("ses :{}".format(self.bilgisayar_Ses))

                else:
                    print("ses zaten en dusukte .....")

            elif cevap == ">":
                if self.bilgisayar_Ses <= 31:

                    print("ses artırıldı.")
                    self.bilgisayar_Ses += 1
                    print("ses :{}".format(self.bilgisayar_Ses))

                else:
                    print("tv ses zaten en yuksekte....")
            else:
                print("ses guncellendi.... ses seviyesi:", self.bilgisayar_Ses)
                break



print("""

        BİLGİSAYAR UYGULAMASI

        1. PC ac

        2. PC kapat

        3. Ses Ayarları

        4. Program Ekle

        5. Bilgisayar bilgileri

        6. Saat Ayarlama
        
        7.

        Cikis icin "q" ya basin...



""")
pc=Bilgisayar()


while True:
    islem = input("islemi seciniz....:")

    if islem == "q":
        print("Program sonlandiriliyor....")
        break

    elif islem == "1":
        pc.acik_Duruma_getir()

    elif islem== "2":
        pc.Kapali_Duruma_getir()

    elif islem=="3":
          pc.ses_Ayarları()

    elif islem=="4":

        while 1:
            secim=input("eklemeye devam etmek icin 'e' ye cikis icin 'q' ya basin..")
            if secim=="e":

                eklenecekler = input("eklenecek programı girin.:")
                if eklenecekler not in pc.programlar:
                    pc.program_ekle(eklenecekler)
                    continue
                else:
                    print("ayni program pc de yuklu")
            else:
                break

    elif islem=="5":
        print(pc)
    elif islem=="6":
        pc.saat_degistirme()
    elif islem=="7":
        pass


        