"""


Problem 6
Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik.
Burada mantık yürüterek ve list comprehension kullanarak

*****1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.******

Not: Programlamada her detayı öğrenemeyiz.
Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur.
Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.

İpucu: Basit düşünmeye çalışın.

"""

print("""


**************************
Programimiza hosgeldiniz
**************************


""")
"""
ilk olarak alıstırma
"""

liste=list()
for i in range(0,20):
    liste.append(i)
print("liste elemanlari=",liste)

print("\n")


liste2=[i for i in range(0,20)]
print("liste2 elemanlari ise =",liste2)
print("\n")

""""
ilk olarak for ile normal bir sekilde 1-100 e kadar olan cift sayilari liste3 atalım sonra list comprehnsiona gecelim..
liste4 e list comprehension uygulayalım...

"""

liste3=list()
for i in range(0,101):
    if i%2==0:
        liste3.append(i)
print("liste3 elemanlari ise=",liste3)
print("\n")

liste4=list()
liste4=[i for i in range(0,101) if i%2==0 ]
print("liste4 elemanlari =",liste4)



liste1=list()
sayi1 = int(input("ilk sayiyi girin      :"))
sayi2 = int(input("aralıgı belirleyecek 2. sayiyi girin    :"))
bölen = int(input("hangi sayiya tam böleni bulmak istiyorsunuz?     :"))

liste1=[ i for i in range(sayi1, sayi2+1) if i%bölen==0 ]
print(liste1)