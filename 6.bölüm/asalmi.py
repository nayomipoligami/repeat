def asal_mi(sayi):
    if (sayi == 1):
        return False

    elif (sayi == 2):
        return True

    else:
        sayac=1
        for i in range(2,sayi):
            sayac+=1
            if (sayi % i == 0):
                return False
            if(i/2==sayac):
                break
        return True

while True:
    sayi = input("sayi:")

    if (sayi == "q"):
        break
    else:
        sayi = int(sayi)
        if (asal_mi(sayi)):
            print(sayi,"asal bir sayidir.")
        else:
            print(sayi,"asal bir sayi degildir.")

