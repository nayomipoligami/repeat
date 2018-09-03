"""
Bölüm 6 Problem 4 - kullanıcıdan alınan 2 basamaklı sayının okunuşunu bulan program
"""


def okunuş_bulma(x):
    if (x < 10 or x > 99):  # Hata yakalama kısmı
        return "Lütfen 10-99 aralığından bir sayı giriniz"
    Onlar = {10: "On", 20: "Yirmi", 30: "Otuz", 40: "Kırk", 50: "Elli", 60: "Altmış", 70: "Yetmiş", 80: "Seksen",
             90: "Doksan"}
    Birler = {0: "", 1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş", 6: "altı", 7: "yedi", 8: "sekiz", 9: "dokuz"}

    birler_b = x % 10
    onlar_b = x - birler_b

    return Onlar[onlar_b] + Birler[birler_b]


print("10-99 aralığında sayı giriniz\tÇıkış için -> q")
while True:
    sayı = input("\nSayı:")
    if (sayı == "q"):
        print("Kapandı")
        break
    sayı = int(sayı)
    print(okunuş_bulma(sayı))