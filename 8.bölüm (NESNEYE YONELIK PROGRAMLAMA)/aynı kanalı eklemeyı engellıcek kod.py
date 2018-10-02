kanal_listesi = ["ATV", "SHOW", "FOX"]  # Kendi Elindeki Kanal Listesi

eklenecek_kanal = input("Eklenecek kanalı giriniz")  # Kullanıcıdan Aldığın İnput

for kanal in kanal_listesi:  # Kanal Değişkeni kanal_listesi içindeki tüm elemanları tek tek oluyor
    if (kanal == eklenecek_kanal):  # Eğer Eklenecek Kanal Listenin İçinde varsa bu bloğa giriyoruz
        print("Kanal Zaten Mevcut")
        break  # Burda Döngüyü Kırmamızın Sebebi yukarıda aldığımız input değeri "ATV"Olduğunu Düşün
        # Döngü başladığında ilk (kanal) değişkenimiz "ATV" Olucak if koşulu sağlanıcak ve
        # Buraya giricek Kanal Zaten Mevcut Diyecek (break) komutunu kullanmaz isek
        # Döngü Burda Devam Edicek (kanal) değişkenimiz "SHOW" Değerini alıcak if e girmiyecek
        # Ve Alttaki Else Bloğuna Girerek ATV Kanalını birden fazla kere ekliyecek
    else:
        kanal_listesi.append(eklenecek_kanal)  # Listemize kanalımızı ekliyoruz
        break  # Yukardaki olay olucak

print(kanal_listesi)

