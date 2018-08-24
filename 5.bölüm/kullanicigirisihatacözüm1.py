k = 1
girişhakkı = 3
kul = {"oguz": "zugo", "kagan": "nagak"}
print(
    "Kullanıcı Girişine Hoşgeldiniz....../n/n************************Eğer giriş yapmak istiyorsanız 'g' tuşunu, eğer kaydolmak istiyorsanız 'k' tuşunu giriniz")
c = input(
    "Lütfen yapmak istediğiniz işlemi seçiniz(giriş yapmak istiyorsanız 'g' kaydolmak istiyorsanız 'k' çıkmak için ise 'ç')")
while 1:
    if c == "ç":
        print("çıkış yapılıyor")
        break
    elif c == "g":
        kulad = input("kullanıcı adınızı giriniz:")
        kul_şifre = input("şifrenizi giriniz:")
        if (kulad in kul.keys() and kul_şifre in kul.values()) :
            print("giriş başarıyla yapıldı.....\n\n")
            break
        else:
            print("şifre yada kullanıcı adı yanlış...")
            girişhakkı -= 1
    elif c == "k":
        kulad = input("kullanmak istediğiniz ismi giriniz:")
        kul[kulad] = input("kullanacağınız şifreyi giriniz:")
        print("kayıt yapıldı.....")
        break

    else:
        print("geçersiz harf tekrar deneyin....")
        break
    if girişhakkı == 0:
        break
