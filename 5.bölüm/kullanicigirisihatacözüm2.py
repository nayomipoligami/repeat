print("""**********************************
\tKullanıcı Girişi Programı
**********************************
""")

sys_username = "detarminant"
sys_password = "12345"

giris_hakki = 3

while True:
    kullanıcı_adı = input("Kullanıcı adı: ")
    sifre = input("Parola: ")
    if (giris_hakki == 0):
        print("Giriş hakkınız kalmadı....")
        break
    else:
        if (giris_hakki == 0):
            print("Giriş hakkınız kalmadı....")
            break
        if (kullanıcı_adı != sys_username and sifre == sys_password):
            print("Kullanıcı adı hatalı")
            giris_hakki -= 1
            print("Kalan giriş hakkı: {}".format(giris_hakki))
        elif (kullanıcı_adı == sys_username and sifre != sys_password):
            print("Parola hatalı")
            giris_hakki -= 1
            print("Kalan giriş hakkı: {}".format(giris_hakki))

        elif (kullanıcı_adı != sys_username and sifre != sys_password):
            print("Kullanıcı adı ve parola hatalı")
            giris_hakki -= 1
            print("Kalan giriş hakkı: {}".format(giris_hakki))

        else:
            print("Giriş yaptınız...")
            break