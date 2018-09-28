def asalsayi():
    secenek=int(input("asal bulma islemine girmek icin 1 e cıkıs yapmak ıcın 2 ye basın....:"))
    while 1:
        if secenek==1:

                a=int(input("kontrol edilcek sayiyi girin:"))
                if a==1:
                    print("asal degil")
                elif a==2 :
                    print("asal")
                else:

                    for i in range(2,a):
                        if a%i==0:
                            print("sayi asal degil")
                            break

                    else:
                        print("sayi asal")
                        continue

        else:
            print("programdan cıkıs yapiliyor...")
            break
asalsayi()