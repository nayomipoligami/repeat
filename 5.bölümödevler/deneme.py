print("""
****************
mükemmel sayı
****************
""")
sayı = int(input("Lütfen bir sayı giriniz: "))
liste = list()

for i in range(1, sayı):

    if sayı % i == 0:
        liste.append(i)

        if sum(liste) == sayı:
            print("Mükemmel sayı")


