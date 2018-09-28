liste=[]
for i in range(1,11):
    liste.append(i)
    if i==10:
        liste.pop(7)
print(liste)

