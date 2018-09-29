import time

"""
Kod bu şekilde. Yapmak istediğim "çalışansorgu" kısmına eğer çalışan veya yönetici birinin ismi girilirse onun bilgileri üzerinde işlem yapmak. 
Tek tek if else sorgularının sayısını arttırmaktansa daha kolay değişken gibi bir çözüm var mı merak ediyorum

"""
class Çalışan():
    def __init__(self, isim, soyisim, maaş, departman):
        self.isim = isim
        self.soyisim = soyisim
        self.maaş = maaş
        self.departman = departman

    def göster(self):
        print("""
              İsim:         {}
              Soyisim:      {}
              Maaş:         {}
              Departman:    {}
              """.format(self.isim, self.soyisim, self.maaş, self.departman))

    def departman_değiştir(self, yeni_departman):
        self.departman = yeni_departman


class Yönetici(Çalışan):
    def zam_yap(self, zam_miktarı):
        self.maaş += zam_miktarı


Tunahan = Yönetici("Tunahan", "Yönetici", 3000, "Ar-Ge")
Taha = Çalışan("Taha", "Çalışan", 1000, "Amele")

while True:
    çalışansorgu = input("Çalışanın İsmini Yazınız: ")

    if çalışansorgu == "Tunahan" or çalışansorgu == "Taha":
        print(Tunahan.göster())

    elif çalışansorgu == "q":
        print("Çıkış Yapılıyor...")
        time.sleep(2)
        break
    else:
        print("İsmi Doğru Giriniz.")
        continue

    zamsorgusu = input("Zam Yapmak İster misiniz?(E/H): ")

    if zamsorgusu == "E" or zamsorgusu == "e":
        zammiktarı = int(input("Yapmak İstediğiniz Zam Miktarını Giriniz: "))
        Tunahan.zam_yap(zammiktarı)
        print(Tunahan.göster())

    elif zamsorgusu == "H" or zamsorgusu == "h":
        print("İşlem İptal Edildi.")

    else:
        print("Doğru karakteri giriniz.")
        break

    departmansorgu = input("Departman Değiştirmek İster misiniz? (E/H): ")

    if departmansorgu == "E" or departmansorgu == "e":
        departmanismi = input("Yapmak İstediğiniz Departman Değişikliğini Giriniz: ")
        Tunahan.departman_değiştir(departmanismi)
        print(Tunahan.göster())

    elif departmansorgu == "H" or departmansorgu == "h":
        print("İşlem İptal Edildi.")
        continue
    else:
        print("Doğru karakteri giriniz.")
        break