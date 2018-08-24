print("""

pisagor ucgenı uzunlukları bulma programına hosgeldiniz....



""")
liste2 = []


def pisagor():
    for i in range(1,101):
        for j in range(1,101):
            c=(i**2+j**2)**0.5
            if c==int(c):
                liste2.append((i,j,c))
    return (liste2)

pisagor()

for i in liste2:
   print(i,end="\n")
print(len(liste2))