def ekok(sayi1, sayi2):
    i = 1
    while True:
        if sayi1 * i % sayi2 == 0:
            print("EKOK:", sayi1 * i)
            break
        i += 1


sayi_1 = int(input("1. sayı: "))
sayi_2 = int(input("2. sayı: "))
ekok(sayi_1, sayi_2)