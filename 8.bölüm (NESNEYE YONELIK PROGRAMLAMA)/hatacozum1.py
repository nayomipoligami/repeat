class bilgisayar():

    def __init__(self,marka="Bilgi Yok",model="Bilgi Yok",renk="Bilgi Yok",tur="Bilgi Yok",boyut="Bilgi Yok"):

        print("init fonksiyonu çağırıldı")



        self.markasi = marka

        self.modeli = model

        self.rengi = renk

        self.turu = tur

        self.boyutu = boyut

    def bilgileriGoster(self):





        print("Bilgisayar markası: {}".format(self.markasi))

        print("Bilgisayar modeli: {}".format(self.modeli))

        print("Bilgisayar rengi: {}".format(self.rengi))

        print("Bilgisayar turu: {}".format(self.turu))

        print("Bilgisayar boyutu: {}".format(self.boyutu))

    def renkDegistir(self,verilenRenk):

        print("Renk değiştiriliyor...")

        self.rengi = verilenRenk





pc1 = bilgisayar("Lenovo","V110","Siyah","Laptop","16inc")





print(pc1.renkDegistir("Kırmızı"))


pc1.bilgileriGoster()