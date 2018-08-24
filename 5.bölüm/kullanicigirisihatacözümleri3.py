#sözlükle kullanici girisi örneği
kul = {"alperen":"nerepla"}
ghak=4
while True:
    print("""//////////////////////
yeni kullanıcı için 'y' harfini giriniz;
kullanıcı girişi için 'k' harfini giriniz;
////////////////////""")
    p= input("==>")
    if p == "y": #yeni kayıt
        kulad= input("isminizi giriniz = ")
        kul[kulad] = input("şifrenizi giriniz = ")
    elif p == "k": #kullanıcı girişi
        kul_ad = input("kullanıcı adınız : ")
        kul_şif = input("kullanıcı şifreniz : ")
        if kul_ad in kul.keys() and kul_şif in kul.values() and kul[kul_ad] == kul_şif:
            print("giriş başarılı...\n\n")
            break
        else:
            print("kullanıcı adınız ve parolanızı yanlış girdiniz...")
            ghak-=1
    else:
        print("geçersiz harf! Tekrar deneyiniz...")
    if ghak == 0:
        print("giriş hakkınız kalmadı...")
        break