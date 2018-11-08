class Hayvan():

    def __init__(self, beslenme, ic_güdü):
        self.beslenme = beslenme
        self.ic_güdü = ic_güdü


class Köpek(Hayvan):

    def __init__(self, beslenme, ic_güdü, ayak_sayisi, cıkardıgı_ses):
        super().__init__(beslenme, ic_güdü)
        self.ayak_sayisi = ayak_sayisi
        self.cıkardıgı_ses = cıkardıgı_ses

    def __len__(self):
        return self.ayak_sayisi

    def __str__(self):
        print("Kopeklerin özellikleri: ")
        return "Beslenme: {} İc Güdü: {} ayak sayilari : {} cıkardıkları ses: {} ".format(self.beslenme, self.ic_güdü,
                                                                                          self.ayak_sayisi,
                                                                                          self.cıkardıgı_ses)


class Kus(Hayvan):

    def __init__(self, beslenme, ic_güdü, ucabilirmi, cıkardıgı_ses):
        super().__init__(beslenme, ic_güdü)
        self.ucabilirmi = ucabilirmi
        self.cıkardıgı_ses = cıkardıgı_ses

    def __str__(self):
        print("Kus ozellıkleri: ")
        return "Beslenme : {} İcgüdü: {} ucma ozelligi : {} cıkardıkları ses: {}".format(self.beslenme, self.ic_güdü,
                                                                                         self.ic_güdü,
                                                                                         self.cıkardıgı_ses)


class At(Hayvan):
    def __init__(self, beslenme, ic_güdü, nal_sayisi, boy):
        super().__init__(beslenme, ic_güdü)
        self.nal_sayisi = nal_sayisi
        self.boy = boy

    def __len__(self):
        return self.nal_sayisi

    def __str__(self):
        print("At özellikleri: ")
        return "Beslenme: {} İc güdü: {} Nal sayisi : {} Boy: {}".format(self.beslenme, self.ic_güdü, self.nal_sayisi,
                                                                         self.boy)


köpek = Köpek("Et yerler", "İc güdüleriyle hareket ederler", 4, "Hav hav")
kus = Kus("Yem yerler", "İc güdüleriyle hareket ederler", "Evet", "Cik Cik")
at = At("Yem yerler", "İc güdüleri kuvvetlidir", 4, "Boylari genellikle 1m 80 cm civarındadır")

print("""
1-Köpek özellikleri
2-Kus özellikleri
3-At özellikleri
Cıkıs ıcın q.
""")

while True:

    secim = input("Secim yapın")

    if (secim == "q"):
        break
    elif (secim == "1"):
        print("Ayak sayilari: ", len(köpek))

        print(köpek)
    elif (secim == "2"):

        print(kus)
    elif (secim == "3"):

        print(at)
        print("Nal sayilari: ", len(at))

    else:
        print("Yanlıs secim")
        break



