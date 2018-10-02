"""

Kodlama Egzersizimizde yazdığımız Kumanda Sınıfına ek olarak metodlar ve özellikler eklemeye çalışın.

***************pycharmda kodları duzene sokma ctrl + alt + L ***************

"""

import time
import random
import datetime
from tkinter import *
window = Tk()


an = datetime.datetime.now()#datetime sınıfından an nesnesini olusturduk..

class Kumanda():
    def __init__(self, tv_durum="kapali", tv_ses=0, kanal_listesi=["trt"],saatim=an.hour,kanal="trt",uydu_Durum="kapali",mevcut_renk="beyaz",renklistesi=["beyaz"]):
        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal

        self.mevcut_renk = mevcut_renk

        self.renklistesi = renklistesi

        self.uydudurum=uydu_Durum

        self.saatim=saatim

    def uyduyu_Ac(self):
        if self.uydudurum=="kapali":

            print("uydu acılıyor..")
            time.sleep(1)
            print("uydu acıldı....iyi seyirler...")
            self.uydudurum="acık"

        else:
            print("uydu zaten acık..")

    def tv_Ac(self):
        if self.tv_durum == "Açık":
            print("tv zaten acık...")
        else:
            print("tv acılıyor...")
            time.sleep(1)

            self.tv_durum = "Açık"

    def tv_Kapat(self):
        if self.tv_durum == "kapali":
            print("tv zaten kapali....")

        else:
            print("tv kapaniyor...")
            self.tv_durum = "kapali"
            time.sleep(1)

    def saat_degistirme(self):
        #ornek olarak eger saat 1 ise saati 1 azalttıgımızda 12 olmalı! bu onemlı!
        while True:

            oynama=input("saati artırmak icin ' + ' azaltmak icin ' - ' ye cikis icin 'q' ye basin: ")
            if oynama=="+":
                if self.saatim>=12 :
                    pass
                else:
                    self.saatim+=1
                    print("saat ayarı yapildi güncel saat:{}".format(self.saatim))
            elif oynama=="-":
                if self.saatim>1:
                    self.saatim-=1
                    print("saat ayarı yapildi güncel saat:{}".format(self.saatim))
                elif self.saatim==1 :
                    self.saatim=12
                    print("saat ayarı yapildi güncel saat:{}".format(self.saatim))
                elif self.saatim==0:
                    self.saatim=11
                elif oynama=="Q" or oynama=="q":
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
                if self.tv_ses != 0:

                    print("ses azaltılıyor...")
                    self.tv_ses -= 1
                    print("ses :{}".format(self.tv_ses))

                else:
                    print("ses zaten en dusukte .....")

            elif cevap == ">":
                if self.tv_ses <= 31:

                    print("ses artırıldı.")
                    self.tv_ses += 1
                    print("ses :{}".format(self.tv_ses))

                else:
                    print("tv ses zaten en yuksekte....")
            else:
                print("ses guncellendi.... ses seviyesi:", self.tv_ses)
                break

    def kanal_ekle(self, new_Channel):
        print("kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(new_Channel)  # boyle kanal eklemis olduk bir seye esitlemeiycez cunku bu bir liste

        print("kanal eklendi...")

    def rastgele_kanal(self):

        rastgele = random.randint(0, len(self.kanal_listesi) - 1)

        self.kanal = self.kanal_listesi[rastgele]  # burada ise kanal rastegele bir kanala atamıs olduk. burası onemlı

        print("suanki kanal", self.kanal)

    def renkdegistir(self):

        time.sleep(1)

        rastgele_renk_secimi = random.randrange(0, len(self.renklistesi) - 1)

        self.mevcut_renk = self.renklistesi[rastgele_renk_secimi]


    def __len__(self):

        return len(self.kanal_listesi)

    def __str__(
            self):  # print kumanda nesnesi yazdıgımızda bize bu fonksiyonu dondursun dıye bu print fonk yerine gecicek..

        return "TV durum : {}\nTv_ses: {}\nKanal_Listesi: {}\nsuankikanal: {}\nsuankirenk :{}\nGüncelSaat:{}".format(self.tv_durum,
                                                                                                        self.tv_ses,
                                                                                                        self.kanal_listesi,
                                                                                                        self.kanal,
                                                                                                        self.mevcut_renk,self.saatim)

print("""

TV UYGULAMASI

1. TV ac

2. TV kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal sayisini ogrenme

6. Rastgele kanal gecme

7. Televizyon bilgileri

8. Renk ekleme

9. Mevcut renkleri gosterme

10. Renk degistir

11. Uyduyu Ac

12. Saat Ayarlama

13. Tarih Ayarlama

Cikis icin "q" ya basin...



""")
kumanda = Kumanda() # kumanda sınıfı olusturup dısarıdan ozellıklerıne erisebilmek icin...


while True:
    islem = input("islemi seciniz....:")

    if islem == "q":
        print("Program sonlandiriliyor....")
        break

    elif islem == "1":

        kumanda.tv_Ac()
        if an.hour>1 and an.hour<5:
            #uyarı buttonu olusturma
            window.title("************")
            window.geometry('200x100')
            lbl = Label(window, text="****bence uyumalısın****")
            lbl.grid(column=10, row=10)
            window.mainloop()

    elif islem == "2":
        kumanda.tv_Kapat()

    elif islem == "3":
        kumanda.ses_Ayarları()

    elif islem == "4":  # bu islem cok onemli!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        kanal_isimleri = input("kanal isimlerini ' , ' ile ayırarak girin....")

        kanal_listesi1 = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi1:
            for i in kanal_listesi1:  # aynı kanalı eklemememek ıcın bu blok olusturuldu..
                if eklenecekler == i:
                    pass
                else:
                    kumanda.kanal_ekle(eklenecekler)

    elif islem == "5":
        print(len(kumanda.kanal_listesi))

    elif islem == "6":
        kumanda.rastgele_kanal()

    elif islem == "7":
        print(kumanda)

    elif islem == "8":
        bas = input(
            "hangi renkleri eklemek istiyorsunuz.. mavi icin ' m ' sari icin ' s ' turuncu icin ' t ' ye basin: ")

        if "turuncu" or "sarı" or "mavi" not in kumanda.renklistesi:

            if bas == "m":
                kumanda.renklistesi.append("mavi")

            elif bas == "s":
                kumanda.renklistesi.append("sarı")

            elif bas == "t":
                kumanda.renklistesi.append("turuncu")
            else:
                print("yanlıs renk secimi girdiniz lutfen dogru giris yapin.")
        else:
            print("mevcut renk zaten var....")


    elif islem == "9":
        print("mevcut renk listesi gosteriliyor.")
        for gösterilcek in kumanda.renklistesi:
            print("renkler :{}".format(gösterilcek), sep="\n")

    elif islem == "10":
        if len(kumanda.renklistesi) > 1:
            print("renl degistirme islemi yapiliyor...")
            kumanda.renkdegistir()
            time.sleep(1)
            print("renk degistirme islemi yapildi...")

        else:
            print("önce renk ekleme yapmalısınız...")

    elif islem == "11":
        if kumanda.tv_durum=="kapali":
            print("önce tv yi ac....!")
        else:
            kumanda.uyduyu_Ac()

    elif islem == "12":
        kumanda.saat_degistirme()


    elif islem == "13":

        pass

    else:
        print("Gecersiz islem......")
