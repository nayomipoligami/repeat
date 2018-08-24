def mukemmelsayi():
    toplam = 0
    bolenler = []
    mukemmeller = []
    for i in range(1, 1001):
        for j in range(1, i):
            if i % j == 0:
                bolenler.append(j)

        for a in bolenler:
            toplam += a

        if toplam == i:
            mukemmeller.append(i)

    print("Mükemmel sayılar:", mukemmeller)


mukemmelsayi()