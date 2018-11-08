"""liste=list()
liste2=list()
eklenen=0
kaclik=int(input("kaclik matris olusturmak istersiniz."))
while True:
    secim=input("eklemek icin e cikmak icin q ya basin:")
    if secim=="e" and eklenen<kaclik :
        eklenen += 1
        sayi=int(input("eklencek sayiyi girin"))
        if eklenen<=kaclik:
            liste2.append(sayi)
            if eklenen==kaclik:
                break
        if len(liste2)==kaclik:
            liste3=list()

    else:
        break
print("liste1 :",liste)

"""
liste1=[[1,3,5],[2,4,1],[1,5,7]]
liste2=[[3,3,4],[2,4,1],[3,5,4]]
liste3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(liste1)):
    for j in range(len(liste2)):
        liste3[i][j]=liste1[i][j]+liste2[i][j]
print(liste3)