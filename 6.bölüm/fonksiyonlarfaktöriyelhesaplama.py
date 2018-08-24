sayi=None
def faktoriyel(sayi):
    sayi = int(input("lutfen neyin faktoriyeli bulunacagini girin:"))
    faktoriyel=1
    i = 1
    while i<=sayi:
        faktoriyel*=i
        i+=1
    print("faktoriyelin sonucu =",faktoriyel)
faktoriyel(sayi)
