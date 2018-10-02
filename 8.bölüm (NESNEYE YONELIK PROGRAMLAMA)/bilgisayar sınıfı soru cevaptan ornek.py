kullanma_kılavuzu = """****************************************
İŞLEMLER:
Ç   : Bilgisayar Simülatöründen Çık
KK  : Kullanma Kılavuzu
AK  : Bilgisayarı Aç/Kapa
BD  : Bilgisayarın Durumunu Görüntüle
PL  : Programları ve Dosyaları Görüntüle
PA  : Program Aç veya Bir Dosyaya Gir
PK  : Program Kapat veya Dosyadan Çık
S># : Ses Ayarla
P># : Parlaklık Ayarla
YP  : Yeni Program Ekle
YD  : Yeni Dosya Oluştur
S   : Dosya veya Program Sil
K   : Kopyala
T   : Taşı
Y   : Yapıştır
****************************************
NOTLAR:
- Bilgisayarı açtığınızda tüm dosyaları ve programları içerisinde bulunduran Ana Sayfada olursunuz. Ana Sayfadan çıkış bilgisayarı kapatmakla mümkündür.

- PL işlemi sadece tek başına girildiğinde o sırada içinde bulunduğunuz dosyanın veya dosya açık değilse ana sayfanın içeriğini gösterir. Eğer bir dosyayı açmadan içeriğini görmek isterseniz path girmelisiniz. Örneğin Ana Sayfada bir A klasörü, A klasöründe ise bir B klasörü bulunsun. Eğer siz Ana Sayfada iken B klasörünün içeriğini görmek istiyorsanız PL>A>B işlemini girebilirsiniz. A klasöründeyken B klasörünün içeriğini görmek isterseniz PL>B işlemini girebilirsiniz.

- Bu simülatördeki programlar işlevsizdir. Sadece açılıp kapanabilirler ve açtığınız programı kapatmasanız bile farklı işlemler gerçekleştirebilirsiniz.

- Ses ve Parlaklık ayarlamalarında # yerine istenilen miktar girilir. Eğer sadece bir doğal sayı girerseniz direkt o düzeye ulaşırsınız. Eğer başına '+' veya '-' alan bir tamsayı girerseniz belirttiğin miktarda arttırma veya azaltma işlemi uygularsınız.

- YP, YD ve S işlemlerinde dosya veya program adı girmeniz istenir. Eğer birden fazla dosya/program oluşturmak veya birden fazla dosya/program silmek istiyorsanız isimler arasına virgül (,) bırakarak girin. Program veya dosya adları şu işaretleri içeremez: , > )

- Aynı dosyanın veya ana sayfanın içinde aynı ismi taşıyan iki dosya, iki program veya bir dosya ve bir program bulunamaz. Bu yüzden böyle bir durumda otomatik olarak bunlar numaralandırılır. Ama karışıklık olmaması için farklı dosyalar içinde bulunan aynı isimli program veya dosya oluşturmaktan kaçının.

- Taşıma işleminde dikkatli olmalısınız. Çünkü bu işlem yapıldığında taşımak istediğiniz dosya veya program hemen bulunduğu konumdan silinir. Eğer yapıştırma işlemini yapmadan bilgisayarı kapatırsanız elinizdeki veriyi kaybedersiniz.
****************************************"""


class Bilgisayar():
    class D():
        def __init__(self, isim, içerik=[], iz=(), ana_sayfa=False):
            self.dosya_ismi = isim
            self.dosya_içeriği = içerik
            self.dosya_izi = iz
            self.ana_sayfa = ana_sayfa

        def __str__(self):
            return self.dosya_ismi

        def __len__(self):
            return len(self.dosya_içeriği)

    class P():
        def __init__(self, isim, iz=()):
            self.program_ismi = isim
            self.program_izi = iz

        def __str__(self):
            return self.program_ismi

    def __init__(self, x1, x2=False, x3=[], x4=50, x5=5, x6=[]):
        self.ana_sayfa = self.D("Ana Sayfa",
                                [self.D(j) for i, j in x1 if i == "D"] + [self.P(j) for i, j in x1 if i == "P"],
                                ana_sayfa=True)
        for i in self.ana_sayfa.dosya_içeriği:
            if type(i) == type(self.D("Dene")):
                i.dosya_izi = (self.ana_sayfa)
            else:
                i.program_izi = (self.ana_sayfa)
        self.bak = x2
        self.hafıza = x3
        self.ses = x4
        self.parlaklık = x5
        self.pano = x6

    def BAK(self):
        if self.bak:
            print("Açık programlar ve bilgisayarınız kapatılıyor.")
            self.hafıza = []
            self.pano = []
            self.bak = False
        else:
            self.bak = True
            self.hafıza = [self.ana_sayfa]
            print("Hoşgeldiniz")

    def BilgisayarDurumu(self):
        if self.bak:
            print("Bilgisayarınız Açık")
            if len(self.hafıza) == 1 and self.hafıza[0] == self.ana_sayfa:
                print("Açık Program veya Dosya Yok")
            else:
                if not self.hafıza[0].ana_sayfa:
                    print("Açık Dosya:", self.hafıza[0])
                if len(self.hafıza) > 1:
                    print("Açık Programlar:", *self.hafıza[1:])
            print("Ses:", self.ses)
            print("Parlaklık:", self.parlaklık)
        else:
            print("Bilgisayarınız Kapalı")

    def Bul(self, tara, bul):
        for i in tara.dosya_içeriği:
            if str(i) == bul:
                return i
        return ()

    def HafızadaBul(self, ara):
        if str(self.hafıza[0]) == ara and not self.hafıza[0].ana_sayfa:
            return self.hafıza[0]
        if len(self.hafıza) < 2:
            return ()
        for i in self.hafıza[1:]:
            if str(i) == ara:
                return i
        return ()

    def İçerikGörüntüleyici(self, x):
        if not self.bak:
            print("Bilgisayarınız kapalı.")
            return
        if len(x) == 1:
            if len(self.hafıza[0]) == 0:
                if self.hafıza[0].ana_sayfa:
                    print("Bilgisayarınız Boş")
                    return
                print("Bu Klasör Boş")
                return
            print(str(self.hafıza[0]) + ":\n", *self.hafıza[0].dosya_içeriği, sep="\n")
        else:
            x.pop(0)
            k = self.hafıza[0]
            while len(x) > 0:
                k = self.Bul(k, x.pop(0))
                if k == ():
                    break
            if k == ():
                print("Hatalı giriş.")
                return
            if len(k) == 0:
                print("Bu Klasör Boş")
                return
            print(str(k) + ":\n", *k.dosya_içeriği, sep="\n")

    def PDAç(self):
        if not self.bak:
            print("Bilgisayarınız kapalı.")
            return
        g = input("Açmak istediğiniz dosyanın veya programın ismini giriniz:")
        pd = self.Bul(self.hafıza[0], g)
        if pd == ():
            print("Bulunduğunuz konumda böyle bir dosya/program yok.")
        else:
            if type(pd) == type(self.D("Dene")):
                self.hafıza[0] = pd
            else:
                self.hafıza.append(pd)
            print(str(pd) + " açıldı.")

    def PDKapa(self):
        if not self.bak:
            print("Bilgisayarınız kapalı.")
            return
        g = input("Kapatmak istediğiniz dosyanın veya programın ismini giriniz:")
        pd = self.HafızadaBul(g)
        if pd == ():
            print("Böyle bir dosya/program açık değil.")
            return
        if type(pd) == type(self.D("Dene")):
            x = self.hafıza[0].dosya_izi[-1]
            self.hafıza[0] = x
        else:
            self.hafıza.remove(pd)
        print(pd, "kapatıldı.")

    def SvPAyarı(self, x, m):
        if m[0] == "+":
            x += int(m[1:])
        elif m[0] == "-":
            x -= int(m[1:])
            if x < 0:
                x = 0
        else:
            x = int(m)
        return x

    def SesAyarı(self, x):
        if not self.bak:
            print("Bilgisayarınız kapalı.")
            return
        self.ses = self.SvPAyarı(self.ses, x)
        if self.ses > 100:
            self.ses = 100
        print("Ses:", self.ses)

    def ParlaklıkAyarı(self, x):
        if not self.bak:
            print("Bilgisayarınız kapalı.")
            return
        self.parlaklık = self.SvPAyarı(self.parlaklık, x)
        if self.parlaklık > 10:
            self.parlaklık = 10
        print("Parlaklık:", self.parlaklık)

    def Arındırıcı(self, x):
        if x.count(">") != 0 or x.count(")") != 0:
            return False
        return True

    def SıfırlayanaKadar(self, x):
        l = [str(i) for i in self.hafıza[0].dosya_içeriği]
        if l.count(x) == 0:
            return x
        if x[-1] == ")":
            s = []
            öl = list(x[:-1])
            öl.reverse()
            for i in öl:
                if i == "(":
                    break
                s.append(i)
            si = ""
            s.reverse()
            for i in s:
                si += i
            ys = str(int(si) + 1)
            yx = x.replace(si + ")", ys + ")")
            return self.SıfırlayanaKadar(yx)
        yx = x + " (2)"
        return self.SıfırlayanaKadar(yx)

    def YeniİzBelirle(self):
        l = [i for i in self.hafıza[0].dosya_izi] + [self.hafıza[0]]
        return tuple(l)

    def YenilerHatalılar(self, x, k):
        y = []
        h = []
        for i in x:
            if not self.Arındırıcı(i):
                h.append(i)
                continue
            d = self.SıfırlayanaKadar(i)
            if k == "D":
                self.hafıza[0].dosya_içeriği.append(self.D(d, iz=self.YeniİzBelirle()))
            else:
                self.hafıza[0].dosya_içeriği.append(self.P(d, iz=self.YeniİzBelirle()))
            y.append(d)
        return (y, h)

    def YvHBastır(self, l, x):
        if len(l[0]) == 0:
            print("Yeni eklenen " + x + " yok.")
        else:
            print("Yeni eklenen " + x + "(lar):", *l[0])
        if len(l[1]) == 0:
            return
        print("Şu " + x + "(lar) , > ) karakterlerinden içerdiğinden eklenmedi:", *l[1])

    def YeniProgram(self):
        if not self.bak:
            print("Bilgisayarınız kapalı.")
            return
        p = input("Eklemek istediğiniz program(lar):").split(",")
        s = self.YenilerHatalılar(p, "P")
        self.YvHBastır(s, "program")

    def YeniDosya(self):
        if not self.bak:
            print("Bilgisayarınız kapalı.")
            return
        d = input("Eklemek istediğiniz dosya(lar):").split(",")
        s = self.YenilerHatalılar(d, "D")
        self.YvHBastır(s, "dosya")

    def HTB(self, x):
        for i in self.hafıza:
            if i == x:
                return True
        return False

    def HafızayıTemizle(self, x):
        if len(self.hafıza) == 1:
            return
        if type(x) == type(self.P("Dene")) and self.HTB(x):
            self.hafıza.remove(x)
        elif type(x) == type(self.D("Dene")):
            n = x.dosya_izi
            k = True
            for i in self.hafıza[1:]:
                p = i.program_izi
                if len(p) <= len(n):
                    continue
                for z in range(0, len(n)):
                    if n[z] != p[z]:
                        k = False
                        break
                if not k:
                    continue
                self.hafıza.remove(i)
        else:
            return

    def Sil(self):
        if not self.bak:
            print("Bilgisayarınız kapalı.")
            return
        if len(self.hafıza[0]) == 0:
            if self.hafıza[0].ana_sayfa:
                print("Bilgisayarınızda zaten hiçbir dosya veya program yok.")
            else:
                print("Bulunduğunuz dosya konumunda zaten herhangi bir dosya veya program yok.")
            return
        g = input("Silmek istediğiniz program(lar)ı veya dosya(lar)ı girin:").split(",")
        s = []
        b = []
        for i in g:
            x = self.Bul(self.hafıza[0], i)
            if x == ():
                b.append(i)
                continue
            s.append(i)
            self.HafızayıTemizle(x)
            self.hafıza[0].dosya_içeriği.remove(x)
        if len(s) == 0:
            print("Silinen dosya veya program yok.")
        else:
            print("Silinen dosya veya programlar:", *s)
        if len(b) != 0:
            print("Bulunduğunuz konumda şu isim(ler)de dosya veya program yok:", *b)

    def Kopyala(self, x="Kopyalayacağınız", d=False):
        if not self.bak:
            print("Bilgisayarınız kapalı.")
            return
        k = self.Bul(self.hafıza[0], input(x + " dosyayı veya programı seçiniz:"))
        if k == ():
            print("Bulunduğunuz konumda böyle bir program veya dosya yok.")
            if d:
                return ()
            return
        self.pano = [k]
        print(str(k), "panoya kopyalandı.")
        if d:
            return k

    def Taşı(self):
        if not self.bak:
            print("Bilgisayarınız kapalı.")
            return
        x = self.Kopyala("Taşıyacağınız", True)
        if x == ():
            return
        self.HafızayıTemizle(x)
        self.hafıza[0].dosya_içeriği.remove(x)

    def Yapıştır(self):
        if not self.bak:
            print("Bilgisayarınız kapalı.")
            return
        if len(self.pano) == 0:
            print("Hiçbir dosya veya program kopyalanmamış.")
            return
        x = self.pano[0]
        if type(x) == type(self.P("Dene")):
            a = self.P(self.SıfırlayanaKadar(str(x)), iz=self.YeniİzBelirle())
            self.hafıza[0].dosya_içeriği.append(a)
        else:
            a = self.D(self.SıfırlayanaKadar(str(x)), iz=self.YeniİzBelirle())
            self.hafıza[0].dosya_içeriği.append(a)
        print(str(a) + " bulunduğunuz dosya konumuna yapıştırıldı.")


b = Bilgisayar([("P", "Hesap Makinesi"), ("P", "Not Defteri"), ("P", "Paint")])

print("BİLGİSAYAR SİMÜLATÖRÜNE HOŞGELDİNİZ\n\nKullanma Kılavuzu için 'KK' giriniz.")

while True:
    g = input("Bir işlem seçiniz:")
    if g == "Ç":
        break
    if g == "KK":
        print(kullanma_kılavuzu)
    elif g == "AK":
        b.BAK()
    elif g == "BD":
        b.BilgisayarDurumu()
    elif len(g) >= 2 and g[:2] == "PL":
        b.İçerikGörüntüleyici(g.split(">"))
    elif g == "PA":
        b.PDAç()
    elif g == "PK":
        b.PDKapa()
    elif len(g) > 2 and g[:2] == "S>":
        b.SesAyarı(g[2:])
    elif len(g) > 2 and g[:2] == "P>":
        b.ParlaklıkAyarı(g[2:])
    elif g == "YP":
        b.YeniProgram()
    elif g == "YD":
        b.YeniDosya()
    elif g == "S":
        b.Sil()
    elif g == "K":
        b.Kopyala()
    elif g == "T":
        b.Taşı()
    elif g == "Y":
        b.Yapıştır()
    else:
        print("Lütfen geçerli bir işlem seçiniz.")