import time
import random


class Hayvan():
    def __init__(self, beslenme, ayak_sayısı, yavru_sayısı):
        self.beslenme = beslenme
        self.ayak_sayısı = ayak_sayısı
        self.yavru_sayısı = yavru_sayısı


class Köpek(Hayvan):
    def __init__(self, beslenme, ayak_sayısı, yavru_sayısı, görev):
        super().__init__(beslenme, ayak_sayısı, yavru_sayısı)
        self.görev = görev

    def __str__(self):
        print("Köpek bilgileri..:")
        return ("Beslenme:{}\nAyak sayısı:{}\nYavru sayısı:{}\nGörev:{}".format(self.beslenme, self.ayak_sayısı,
                                                                                self.yavru_sayısı, self.görev))

    def __len__(self):
        print("Köpek ayak Sayısı..:")
        return (self.ayak_sayısı)


class Kuş(Hayvan):
    def __init__(self, beslenme, ayak_sayısı, yavru_sayısı, görev, kanat_sayısı):
        super().__init__(beslenme, ayak_sayısı, yavru_sayısı)
        self.görev = görev
        self.kanat_sayısı = kanat_sayısı

    def __str__(self):
        print("Kuş bilgileri..:")
        return ("Beslenme:{}\nAyak sayısı:{}\nYavru sayısı:{}\nGörev:{}\nKanat Sayısı:{}".format(self.beslenme,
                                                                                                 self.ayak_sayısı,
                                                                                                 self.yavru_sayısı,
                                                                                                 self.görev,
                                                                                                 self.kanat_sayısı))

    def __len__(self):
        print("Kuş kanat sayısı Sayısı..:")
        return (self.ayak_sayısı)


class At(Hayvan):
    def __init__(self, beslenme, ayak_sayısı, yavru_sayısı, görev, ağırlık):
        super().__init__(beslenme, ayak_sayısı, yavru_sayısı)
        self.görev = görev
        self.ağırlık = ağırlık

    def __str__(self):
        print("At Bilgileri..:")
        return (
            "Beslenme:{}\nAyak sayısı:{}\nYavru sayısı:{}\nGörev:{}\nAğırlık:{}".format(self.beslenme, self.ayak_sayısı,
                                                                                        self.yavru_sayısı, self.görev,
                                                                                        self.ağırlık))

    def __len__(self):
        print("ağırlık..:")
        return (self.ağırlık)


köpek = Köpek("Et", 4, 6, "koruma")
kuş = Kuş("Yem", 2, 4, "Uçmak", 2)
at = At("ot", 4, 1, "Ulaşım", 300)

print("""********************************
HAYVAN BİLGİLERİ
1-KUŞ
2-KÖPEK
3-AT
4-RASTGELE SEÇİM
q-çıkış
**********************************
""")
while True:
    işlem = input("İşleminizi seçiniz....:")
    if (işlem == "q"):
        print("Çıkılıyor...")
        break
    elif (işlem == "1"):
        print("bilgilere ulaşmaya çalışıyorum....")
        time.sleep(1)
        print(kuş)
    elif (işlem == "2"):
        print("bilgilere ulaşmaya çalışıyorum....")
        time.sleep(1)
        print(köpek)
    elif (işlem == "3"):
        print("bilgilere ulaşmaya çalışıyorum....")
        time.sleep(1)
        print(at)
    elif (işlem == "4"):
        seçim = random.randint(1, 3)
        if (seçim == "1"):
            print("bilgilere ulaşmaya çalışıyorum....")
            time.sleep(1)
            print(kuş)
        elif (seçim == 2):
            print("bilgilere ulaşmaya çalışıyorum....")
            time.sleep(1)
            print(köpek)
        elif (seçim == 3):
            print("bilgilere ulaşmaya çalışıyorum....")
            time.sleep(1)
            print(at)
    else:
        print("Hatalı Seçim : Tekrar Deneyiniz....")
