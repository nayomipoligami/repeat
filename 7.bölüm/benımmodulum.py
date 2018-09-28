def toplama ():
    """"
    bu fonksiyon toplama islemi yapar..

    """
    soru = input("Toplanacak sayilari araya '-' koyarak yaziniz.\n")
    soru = soru.split("-")
    top = 0
    for i in range(0, len(soru)):
        top += int(soru[i])
    return print(top)


def cikarma (x,y):
    """"
    bu fonksiyon cikarma islemi yapar..

    """
    return x-y

def carpma (x,y):
    """"
    bu fonksiyon carpma islemi yapar..

    """
    return x*y

def bölme (x,y):
    """"
    bu fonksiyon bölme islemi yapar..

    """
    return float(x/y)


s="lalalala"
for i in reversed(s):
    print(i,end="")


