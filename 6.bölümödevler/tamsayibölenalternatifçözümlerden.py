def bölenler (a):
    if (a == 0):
        return 0
    else:
        while True:
            liste = []
            for i in range(1,a+1):
                if (a % i == 0):
                    liste.append(i)
            print("Girilen Sayının Tam Bölenleri:{}".format(liste))
            break
bölenler(24)