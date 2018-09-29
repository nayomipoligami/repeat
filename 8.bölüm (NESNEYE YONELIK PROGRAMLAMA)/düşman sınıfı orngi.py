import random


class savaş():
    def __init__(self, isim="Düşman", can=500, güç=50, mermi_sayısı=10):
        self.isim = isim
        self.can = can
        self.güç = güç
        self.mermi_sayısı = mermi_sayısı

    def saldır(self):
        print(self.isim + " saldırıyor")
        harcanan_mermi_sayısı = random.randrange(1, self.mermi_sayısı)
        self.mermi_sayısı -= harcanan_mermi_sayısı
        print(self.isim + " " + str(harcanan_mermi_sayısı) + " kadar mermi harcadı." + str(
            self.mermi_sayısı) + " kadar mermisi kaldı.")

        return harcanan_mermi_sayısı * self.güç

    def saldırıya_uğra(self, alınan_hasar):
        self.can -= alınan_hasar
        print(self.isim + " saldırıya uğradı." + str(self.can) + " kadar canı kaldı.")

    def hayatta_mı(self):
        if (self.can) <= 0:
            print(self.isim + " öldü")
            return False
        else:
            print(self.isim + " hala hayatta.")
            return True

    def mermi_kaldı_mı(self):
        if (self.mermi_sayısı) <= 0:
            print(self.isim + "'in mermisi kalmadı.")
            return False
        else:
            print(self.isim + "'in mermisi var.")
            return True

    def print(self):
        print("İsim:{}  Canı:{}   Gücü:{}    Mermi Sayısı:{}".format(self.isim, self.can, self.güç, self.mermi_sayısı))


düşmanlar = list()
i = 0
while i < 5:
    rastgele_can = random.randrange(1, 500)
    rastgele_güç = random.randrange(1, 50)
    rastgele_mermi_sayısı = random.randrange(1, 10)
    düşman = savaş("Düşman" + str(i + 1), rastgele_can, rastgele_güç, rastgele_mermi_sayısı)
    düşmanlar.append(düşman)
    i += 1

for düşman in düşmanlar:
    düşman.print()

i = 0
while i < 3:
    saldırcak_düşman = random.randrange(0, 4)
    saldırıya_uğrucak_düşman = random.randrange(0, 4)
    if saldırcak_düşman == saldırıya_uğrucak_düşman:
        continue
    else:
        if düşmanlar[saldırıya_uğrucak_düşman].hayatta_mı():
            if düşmanlar[saldırcak_düşman].hayatta_mı():
                if düşmanlar[saldırcak_düşman].mermi_kaldı_mı():
                    dönen_değer = düşmanlar[saldırcak_düşman].saldır()
                    düşmanlar[saldırıya_uğrucak_düşman].saldırıya_uğra(dönen_değer)
                    print("Raund bitti..")
                    i += 1
        else:
            continue