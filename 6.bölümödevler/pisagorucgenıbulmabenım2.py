liste1 = list()
def pisagor():

    i=1
    j=1
    sayac=0
    while i<101:
        while j<101:
            c=(i**2+j**2)**1/2
            if c == int(c):
                liste1.append((i,j,c))
                sayac+=1
            j+=1
        i+=1
    print(sayac)
    return liste1

liste2=[i for i in liste1]
pisagor()

for t in liste2:
    print(t)
print(len(liste2))


