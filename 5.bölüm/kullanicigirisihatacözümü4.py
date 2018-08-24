print("""************************
Kullanıcı Girişi Programı

**************************""")
print("Kaydolmak İçin 1 e Giriş Yapmak İçin 2 ye Basınız...")
a = int(input("İsteğinize Göre 1 veya 2 ye Basınız:"))
if (a == 1):
    Kullanıcı_Adı = input("Kullanıcı Adınızı Giriniz:")

    Parola1 = input("Parolanızı  Giriniz:")
    Parola2 = input("Parolanızı 2. defa giriniz")
    if (Parola1 != Parola2):
        print("Parolalar Uyuşmuyor!")

    e_posta = input("Geçerli Bir E-posta Adresi Giriniz:")
    print("E-postanıza Onay Maili Gönderilmiştir...\nKaydınız Tamamlanmıştır,Onay Mailinize Bakmayı Unutmayınız.")

elif (a == 2):
    sys_kullanıcı_adı = "gorgenyilmaz"
    sys_parola = "12345"
    giris_hakkı = 3

    while True:
        Kullanıcı_adı = input("Kullanıcı Adını Giriniz:")
        parola = input("Parolayı Giriniz:")
        if (sys_kullanıcı_adı == Kullanıcı_adı and sys_parola != parola):
            print("Parola Hatalı...")
            print("Şifrenizi mi Unuttunuz?")
            s = int(input("Unuttuysanız 1 e basınız:"))
            if s == 1:
                Yeni_Şifre = input("Yeni şifrenizi  giriniz:")
                Yeni_Şifre2 = input("Yeni şifrenizi ikinci defa giriniz:")
                if (Yeni_Şifre != Yeni_Şifre2):
                    print("Şifreler Uyuşmuyor!")
                else:
                    e_posta = input("Lütfen E-Posta Adresinizi Giriniz:")
                    print("Şifreniz başarıyla değiştirildi\nE-postanıza gelen onay mailine bakmayı unutmayınız!")


        elif (sys_kullanıcı_adı != Kullanıcı_adı and sys_parola != parola):
            print("Kullanıcı Adı ve Parola Hatalı...")
            print("Parola Hatalı...")
            print("Şifrenizi mi Unuttunuz?")
            s = int(input("Unuttuysanız 1 e basınız:"))
            if s == 1:
                Yeni_Şifre = input("Yeni şifrenizi  giriniz:")
                Yeni_Şifre2 = input("Yeni şifrenizi ikinci defa giriniz:")
                if (Yeni_Şifre != Yeni_Şifre2):
                    print("Şifreler Uyuşmuyor!")
                else:
                    e_posta = input("Lütfen E-Posta Adresinizi Giriniz:")
                    print("Şifreniz başarıyla değiştirildi\nE-postanıza gelen onay mailine bakmayı unutmayınız!")
        elif (sys_kullanıcı_adı == Kullanıcı_adı and sys_parola == parola):
            print("Sisteme Giriş Yapılıyor...")
            break

        else:
            print("Kullanıcı Adı Hatalı...")
        giris_hakkı -= 1
        if (giris_hakkı == 0):
            print("Giriş Hakkınız Doldu!")
            break