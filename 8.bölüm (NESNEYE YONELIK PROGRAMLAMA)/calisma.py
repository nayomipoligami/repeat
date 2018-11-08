
import time
liste2=list()
class liste():
    def __init__(self):
        pass


    def listeye_eleman_Ekleme(self):
        while 1:
            secim=input("eklemek icin 1 e listeden eleman cıkarmak icin icin 2 ye basin: cikis icin q ya listenin tersini buldurmak icin t ye basin:")
            if secim=="1":

                    sayi=input("listeye eklenicek sayiyi girin:")
                    sayi=int(sayi)
                    if sayi in liste2:
                        print("ayni eleman zaten var...ekleyemezsiniz")
                    else:

                        liste2.append(sayi)


            elif secim=="2":
                print("listeden hangi elemani cikartmak istiyorsunuz?",liste2)
                cikartilcak=int(input("cikartilcak sayiyi girin:"))
                if cikartilcak in liste2:
                    print("cikartilan sayinin indexi {}".format(liste2.index(cikartilcak)))
                    liste2.remove(cikartilcak)
                    time.sleep(1)
                    print("cıkartıldı.")
                elif len(liste2)==0:
                    print("liste boş cıkartilcak eleman yok.")
                else:
                    print("eleman listede yok.")
            elif secim=="t":
                print("listenin tersi",liste2[::-1])
            else:
                break
liste3=liste()

liste3.listeye_eleman_Ekleme()

print(liste2)
