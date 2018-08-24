print("""*****************************************
Atm'ye Hoşgeldiniz.

Yapmak İstediğiniz İşlemi Seçin:

1 - Bakiye Sorgulama
2 - Para Yatırma
3 - Para Çekme
4 - Havale Yapma/Sorgulama(Havale Ücreti 4 TL Olarak Ücretlendirilecektir.)
5 - Kredi Çekme(Kredi Faizi %5 olarak borcunuza eklenecektir.)
6 - Borç Ödeme/Sorgulama

Çıkış Yapmak için '0' ı Tuşlayın.
*****************************************
""")

bk = 10000
borc = 0
bkredi = 50000

while True:
    islem = input("İşlem: ")
    if islem == "0":
        print("\nYine Bekleriz...")
        break
    elif islem == "1":
        print("Bakiyeniz {} TL dir.".format(bk))
        continue
    elif islem == "2":
        while True:
            yatp = int(input("Yatırılacak Parayı girin(Çıkmak için '0'a basın.): "))
            yatp = abs(yatp)
            if yatp == 0:
                print("Çıkılıyor...")
                break
            print("Yatırılacak Para: {} TL dir.".format(yatp))
            onay = input("Onaylıyor musunuz? (E/H)")
            if onay == "E":
                print("Paranızı Makinenin Sağ alt Köşesine Yerleştirin.\nBanknot Okunuyor...")
                bk += yatp
                print("Yeni Bakiye: {} TL dir.".format(bk))
                yenileme = input("Yeniden Para Yatırmak İstermisiniz?(E/H)")
                if yenileme == "E":
                    continue
                elif yenileme == "H":
                    break
                else:
                    print("Hatalı Giriş, İşleminiz İptal Ediliyor...")
                    break
            elif onay == "H":
                print("İşleminiz İptal Edildi.")
                continue
            else:
                print("Hatalı Giriş, İptal Ediliyor...")
                break
    elif islem == "3":
        while True:
            cekp = int(input("Çekilecek Parayı Giriniz(Çıkmak için '0'a basın.): "))
            cekp = abs(cekp)
            if cekp == 0:
                print("Çıkılıyor...")
                break
            elif cekp < bk:
                print("Çekilecek Para: {} TL dir.".format(cekp))
                onay = input("Onaylıyor musunuz? (E/H)")
                if onay == "E":
                    print("Paranızı Makinenin Sağ Alt Köşesinden Alın.")
                    bk -= cekp
                    print("Yeni Bakiye: {} TL dir.".format(bk))
                    yenileme = input("Yeniden Para Çekmek İstermisiniz?(E/H)")
                    if yenileme == "E":
                        continue
                    elif yenileme == "H":
                        break
                    else:
                        print("Hatalı Giriş, İşleminiz İptal Ediliyor...")
                        break
                elif onay == "H":
                    print("İşleminiz İptal Edildi.")
                    continue
                else:
                    print("Hatalı Giriş, İptal Ediliyor...")
                    break
            else:
                print("Yetersiz Bakiye, Bakiyeniz: {} TL dir.".format(bk))
                continue
    elif islem == "4":
        while True:
            havp = int(input("Havale Yapılacak Miktar(Çıkmak için '0'a basın.): "))
            havp = abs(havp)
            if havp == 0:
                print("Çıkılıyor...")
                break
            elif havp < bk:
                havnum = int(input("Havale Yapılacak Banka Numarası: "))
                print("Havale Yapılacak Para: {} TL\nBanka Numarası: {}".format(havp, havnum))
                onay = input("Onaylıyor musunuz? (E/H)")
                if onay == "E":
                    print("Havale Başarıyla Gerçekleştirildi.")
                    bk -= havp
                    bk -= 4
                    print("Yeni Bakiye: {} TL dir".format(bk))
                    yenileme = input("Yeniden Havale Yapmak İster misiniz?(E/H)")
                    if yenileme == "E":
                        continue
                    elif yenileme == "H":
                        break
                    else:
                        print("Hatalı Giriş, İşleminiz İptal Ediliyor...")
                        break
                elif onay == "H":
                    print("İşleminiz İptal Edildi.")
                    continue
                else:
                    print("Hatalı Giriş, İptal Ediliyor...")
                    break
            else:
                print("Yetersiz Bakiye, Bakiyeniz: {} TL dir.".format(bk))
                continue
    elif islem == "5":
        while True:
            if bkredi <= 0:
                print("Bankadan daha fazla kredi çekemezsiniz.")
                break
            kredi = int(input("Kredi Çekilecek Miktar(Çıkmak için '0'a basın.): "))
            kredi = abs(kredi)
            if kredi == 0:
                print("Çıkılıyor...")
                break
            elif kredi <= 50000:
                print("Kredi Çekilecek Para: {} TL\nBorcunuz: {} TL".format(kredi, (kredi * 5 / 100) + kredi))
                onay = input("Onaylıyor musunuz? (E/H)")
                if onay == "E":
                    bkredi -= kredi
                    print("Kredi bakiyenize eklenmiştir.")
                    bk += kredi
                    borc += (kredi * 5 / 100) + kredi
                    borc = float(borc)
                    print("Yeni Bakiye: {} TL dir".format(bk))
                    yenileme = input("Yeniden Kredi Çekmek İster misiniz?(E/H)")
                    if yenileme == "E":
                        continue
                    elif yenileme == "H":
                        break
                    else:
                        print("Hatalı Giriş, İşleminiz İptal Ediliyor...")
                        break
                elif onay == "H":
                    print("İşleminiz İptal Edildi.")
                    continue
                else:
                    print("Hatalı Giriş, İptal Ediliyor...")
                    break
            else:
                print("En fazla '50000 TL' kredi çekebilirsiniz.")
                continue
    elif islem == "6":
        print("""********************\n1- Borç Ödeme\n2- Borç Sorgulama\n3- Geri Gidin\n********************""")
        while True:
            islem2 = input("İşlemi Giriniz: ")
            if islem2 == "1":
                if borc != 0:
                    while True:
                        odenenpara = int(input("Ödenecek Miktar(Çıkmak için '0'a basın.): "))
                        odenenpara = abs(odenenpara)
                        if odenenpara == 0:
                            print("Çıkılyor...")
                            break
                        if odenenpara > bk:
                            print("Bakiyeniz Yetersizdir, Bakiyeniz {} TL dir.".format(bk))
                            continue
                        else:
                            print("Ödenecek Para: {} TL dir.".format(odenenpara))
                            onay = input("Onaylıyor musunuz? (E/H)")
                            if onay == "E":
                                print("Borcunuzun {} TL'si ödenmiştir.".format(odenenpara))
                                borc -= odenenpara
                                print("Borcunuz: {} TL dir.".format(borc))
                                break
                            elif onay == "H":
                                print("İşleminiz İptal Edildi.")
                                continue
                            else:
                                print("Hatalı Giriş, İptal Ediliyor...")
                                break
                else:
                    print("Borcunuz Bulunmamaktadır.")
            elif islem2 == "2":
                print("Borcunuz {} TL dir.".format(borc))
            elif islem2 == "3":
                print("Çıkılıyor...")
                break
            else:
                print("Geçersiz İşlem!")
                continue
    else:
        print("Geçersiz İşlem!")
        continue