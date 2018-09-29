#ornek alıstırmalar

print("""

Alıstırmalara hosgeldiniz.........



""")

class araba():

    def __init__(self,model,renk,beygir_gücü,silindir):

            self.model=model
            self.renk=renk
            self.beygir_gücü=beygir_gücü
            self.silindir=silindir

bmw=araba("bmw 4 kasa","lacivert",190,4)



print(bmw.model,bmw.renk,bmw.beygir_gücü,bmw.silindir,sep="***")

"""

hocam şu soru nasıl yapılır yardımcı olur musunuz. 

öğretmenler adında bir sınıf tanımlanacak.
sınıfın özelliklerinde öğretmen ismi,bölümü,haftalık girdiği ders saati,verdiği dersler olacak.ders saat ücreti 15 tl
olarak özelliklerde tutulacak.aylık aldığı ders saati hesaplanan method yazılacak.
verdiği derslere ekleme çıkarma methodları yazılacak


bu ornegi diger dersleri izleyip yappp....


"""


print("diger program************************")
class pc():

    def __init__(self, sistem='', işlemci='', anakart='', ekrankartı='', ram='', ssd=''):
        self.sistem=sistem
        self.islemci=işlemci
        self.kart=anakart
        self.ekrankart=ekrankartı
        self.ram=ram
        self.ssd=ssd

user1_pc=pc("win10","i7","acer gaming","gtx1050","16gb","250gb")
user2_pc=pc("linux","i7","asus gaming","gtx950m","16gb","500gb")

print("user1 ssd :{}  user2 ssd : {}".format(user1_pc.ssd,user2_pc.ssd))








