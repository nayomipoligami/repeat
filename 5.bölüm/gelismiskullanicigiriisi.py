import time
import ctypes  # An included library with Python install.
print("""
*******

KULLANİCİ GİRİŞİ PROGRAMINA HOSGELDİNİZ...

*******


""")
# Sözlük oluşturalım.
sozluk = {"system":12345}
sys_kullaniciadi="system"

sys_parola="12345"
giris_hakki=3
giris=input("yeni kayit icin k' ye  giris icin g' ye basiniz...")
while 1:
    if giris=="g":#giris islemi icin...
        while True:

            username=input("lutfen kullanici adinizi girin...:")
            parola=input("lutfen paolanizi girin...:")

            if username in sozluk.keys() and parola in sozluk.values() and sozluk[username]==username and sozluk[parola]==parola  :
                print("kullanici adi ve parolaniz dogru basariyla giris yapiliyor...")
                time.sleep(3)
                print("tebrikler giris yapildi....")
                break
            elif username==sys_kullaniciadi and parola!=sys_parola:
                print("parolaniz yanlis lutfen tekrar deneyin..")
                giris_hakki-=1
                if(giris_hakki==0):
                    print("giris hakkiniz bitti ....")
                    time.sleep(3)
                    print("ERROR ERROR ERROR!!!!!")
                    print("programdan cikiliyor...")
                    break
            elif username != sys_kullaniciadi and parola == sys_parola:
                print("kullanici adiniz yanlis lutfen tekrar deneyin..")
                giris_hakki -= 1
                if (giris_hakki == 0):
                    print("giris hakkiniz bitti ....")
                    time.sleep(3)
                    print("ERROR ERROR ERROR!!!!!")
                    print("programdan cikiliyor...")
                    break
            else:
                print("parolaniz ve kullanici adiniz yanlis lutfen tekrar deneyin..")
                giris_hakki -= 1
                if (giris_hakki == 0):
                    print("giris hakkiniz bitti ....")
                    ctypes.windll.user32.MessageBoxW(0, "hatalı giriş !", "!ERROR!", 1)
                    time.sleep(3)
                    print("programdan cikiliyor...")
                    break
    elif giris=="k":#yeni kayıt icin..
        print("yeni kayit isleminiz baslatiliyor...")
        time.sleep(2)
        yeni_username=input("lutfen yeni bir kullanici adi girin..")
        yeni_parola=input("lutfen yeni bir parola girin...")
        sozluk.update({yeni_username: yeni_parola})
        print(sozluk)
        continue