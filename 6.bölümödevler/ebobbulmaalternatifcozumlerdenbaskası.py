def ebob(a, b):
    for i in range(1, a + 1):
        if a % i == 0:
            if b % i == 0:
                ebob = i
    return ebob


print(""" EBOB BULMA PROGRAMI

ÇIKMAK İÇİN 1 YA DA 2. SAYI DEĞERİNE Q GİRİN """)

while True:
    x = input("1. sayıyı girin:")
    y = input("2. sayıyı girin:")

    if x == "q" or y == "q":
        print("Çıkılıyor...")
        break
    else:
        x = int(x)
        y = int(y)
        print("Girilen sayıların EBOB değeri:", ebob(x, y))
