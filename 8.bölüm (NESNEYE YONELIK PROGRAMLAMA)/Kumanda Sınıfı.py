import time
import random

class Kumanda():
    def __init__(self,tv_durum="kapali",tv_ses=0,kanal_listesi=["trt"],kanal="trt"):
        self.tv_durum=tv_durum

        self.tv_ses=tv_ses

        self.kanal_listesi=kanal_listesi

        self.kanal=kanal

    def tv_Ac(self):
        if self. tv_durum=="Açık":
            print("tv zaten acık...")
        else:
            print("tv acılıyor...")
            time.sleep(1)

            self.tv_durum="Açık"

    def tv_Kapat(self):
        if self.tv_durum=="kapali":
            print("tv zaten kapali....")

        else:
            print("tv kapaniyor...")
            self.tv_durum="kapali"
            time.sleep(1)
    def ses_Ayarları(self):
         while True:
             cevap=input("sesi azalt :'< '\n sesi arttır '>'\n cikis : 'cikis' " )

             if cevap =="<":
                 if self.tv_ses!=0:

                     print("ses azaltılıyor...")
                     self.tv_ses-=1
                     print("ses :{}".format(self.tv_ses))

                 else:
                     print("ses zaten en dusukte .....")

             elif cevap==">":
                 if self.tv_ses<=31:

                     print("ses artırıldı.")
                     self.tv_ses+=1
                     print("ses :{}".format(self.tv_ses))

                 else:
                     print("tv ses zaten en yuksekte....")
             else:
                 print("ses guncellendi.... ses seviyesi:",self.tv_ses)
                 break
    def kanal_ekle(self,new_Channel):
        print("kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(new_Channel) # boyle kanal eklemis olduk bir seye esitlemeiycez cunku bu bir liste

        print("kanal eklendi...")

    def rastgele_kanal(self):

        rastgele=random.randint(0,len(self.kanal_listesi)-1)

        self.kanal=self.kanal_listesi[rastgele] #burada ise kanal rastegele bir kanala atamıs olduk. burası onemlı

        print("suanki kanal",self.kanal)


    def __len__(self):

         return len(self.kanal_listesi)

    def __str__(self): #print kumanda nesnesi yazdıgımızda bize bu fonksiyonu dondursun dıye bu print fonk yerine gecicek..

        return "TV durum : {}\nTv_ses: {}\nKanal_Listesi: {}\nsuankikanal: {}\n ".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)



print("""

TV UYGULAMASI

1. TV ac

2. TV kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal sayisini ogrenme

6. Rastgele kanal gecme

7. Televizyon bilgileri

Cikis icin "q" ya basin...



""")
kumanda=Kumanda()

while True:
    islem=input("islemi seciniz....:")

    if islem=="q":
        print("Program sonlandiriliyor....")
        break

    elif islem=="1":
        kumanda.tv_Ac()

    elif islem=="2":
        kumanda.tv_Kapat()

    elif islem=="3":
        kumanda.ses_Ayarları()

    elif islem=="4": #bu islem cok onemli!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        kanal_isimleri=input("kanal isimlerini ' , ' ile ayırarak girin....")

        kanal_listesi1 = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi1:
            kumanda.kanal_ekle(eklenecekler)

    elif islem=="5":
        print(len(kumanda.kanal_listesi))

    elif islem=="6":
        kumanda.rastgele_kanal()

    elif islem=="7":
        print(kumanda)


    else:
        print("Gecersiz islem......")

