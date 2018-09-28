def asal(a):
    bölüm = []
    for i in range(1, (a + 1)):
        if a % i != 0:
            continue
        elif a % i == 0:
            bölüm.append(i)
    if len(bölüm) == 2:
        return True
    else:
        return False


while True:
    a = int(input("Sayıyı giriniz: "))
    if a == "q":
        break
    else:
        if asal(a) == True:
            print(a, "Bir asal sayıdır")
        else:
            print(a, "Bir asal sayı değildir")
