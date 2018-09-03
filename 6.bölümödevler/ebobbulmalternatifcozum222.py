def ebobbulma(a, b):
    ebob = 1
    for i in range(1, a and b):
        if (a % i == 0 and b % i == 0):
            ebob = i
    print("ebob= ", ebob)


a = int(input("İlk sayı"))
b = int(input("İkinci sayi"))

ebobbulma(a, b)



