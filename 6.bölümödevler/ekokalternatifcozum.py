def ekok(x, y):
    ekok = 0
    i = 1
    while True:
        if i % x == 0 and i % y == 0:
            ekok = i
            break
        i += 1
    print(ekok)
    return ekok


x = int(input("1. sayı"))
y = int(input(("2. sayı")))
ekok(x, y)



