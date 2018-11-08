print("""

Proje 3
Bu projede ise 4 tane sınıfı oluşturun.

Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.


""")
import time

class Hayvan():
    def __init__(self,speed=0,power=0,ayak_Sayisi=0,cinsler=list(),kuyruk=False,zeka=0):


        self.speed=speed
        self.power=power
        self.ayak_Sayisi=ayak_Sayisi
        self.cinsler=cinsler
        self.kuyruk=kuyruk
        self.zeka=zeka

    def __str__(self):
        print("hayvanin özellikleri:\n")
        return "speed:{}\npower:{}\nayak_Sayisi:{}\ncinsler:{}\nkuyruk:{}\zeka:{}\n".format(self.speed,self.power,self.ayak_Sayisi,
                                                                                            self.cinsler,self.kuyruk,self.zeka)

    """
    def __del__(self):
        print("hayvan siliniyor...")
    """
    def hizlandir(self,artis_miktari):
        while True:
            hiz_Secim=input("devam etmek icin d ye cikis icin q ya basin... ")
            if hiz_Secim=="d":

                artis_miktari=int(input("hizi artirmak istediginiz miktari girin:"))
                self.speed+=artis_miktari
                time.sleep(1)
                return "hiz güncellendi. güncel hiz:{}".format(self.speed)
            else:
                break

    def yavaslat(self,azaltma_miktari):
        while True:
            hiz_Secim=input("devam etmek icin d ye cikis icin q ya basin... ")
            if hiz_Secim=="d":
                azaltma_miktari = int(input("hizi azaltmak istediginiz miktari girin:"))
                self.speed-=azaltma_miktari
                time.sleep(1)
                return "hiz güncellendi. güncel hiz:{}".format(self.speed)
            else:
                break


class Köpek(Hayvan):
    def __init__(self,tirnak_Sayisi=0):
        super().__init__(self,speed=0,power=0,ayak_Sayisi=0,cinsler=list(),kuyruk=False,zeka=0)
        self.tirnak_Sayisi=tirnak_Sayisi
    def tirnak(self):
        secim=int(input("cift tirnak mi tek tirnak mi oldugunu girin:"))
        if secim=="tek":
            self.tirnak_Sayisi+=1
            time.sleep(1)
            print("tirnak sayisi güncellendi...")
        else:
            self.tirnak_Sayisi+=2
            time.sleep(1)
            print("tirnak sayiisi güncellendi...")


    def hizlandir(self, artis_miktari):
        super().hizlandir()
    def yavaslat(self,azaltma_miktari):
        super().yavaslat()


class Kuş(Hayvan):
    def __init__(self,kuyruk_rengi=["mavi","sari"],güncel_renk="mavi"):
        super().__init__(self,speed=0,power=0,ayak_Sayisi=0,cinsler=list(),kuyruk=False,zeka=0)
        self.kuyruk_rengi=kuyruk_rengi
        self.güncel_renk=güncel_renk

    def hizlandir(self, artis_miktari):
        super().hizlandir()


    def yavaslat(self,azaltma_miktari):
        super().yavaslat()



    def kuyruk_Renk_güncelleme(self):

        seciminiz=input("kuyruk rengi ekleyin veya secin, eklemek icin e secmek icin s ye basin ,cikmak icin q ya basin")
        while 1:
            if seciminiz=="e":
                eklencek_Renk=input("eklemek istediginiz rengi girin:")
                self.kuyruk_rengi.append(eklencek_Renk)
                time.sleep(1)
                print("renk eklendi..")
            elif seciminiz=="s":
                print("listedeki renkler:",self.kuyruk_rengi)
                renk=input("secmek istediginiz renk:?")

                for renk in self.kuyruk_rengi:
                    if renk in self.kuyruk_rengi:
                        self.güncel_renk=renk

            else:
                break

    def hizlandir(self, artis_miktari):
            super().hizlandir()


class At(Hayvan):

    def __init__(self,cinsi):
        super().__init__(self,speed=0,power=0,ayak_Sayisi=0,cinsler=list(),kuyruk=False,zeka=0)


    def hizlandir(self,artis_miktari):
        super().hizlandir()

    def yavaslat(self,azaltma_miktari):
        super().yavaslat()


Kus=Kuş()