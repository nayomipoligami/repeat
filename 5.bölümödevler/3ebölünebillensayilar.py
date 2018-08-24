"""


Problem 5
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.

"""
print("""

Programimiza hosgeldiniz....


""")

for i in range(1,101):

    if i%3!=0:
        continue
    print("{} sayisi 3 ile tam bölünebiliyor...".format(i))



