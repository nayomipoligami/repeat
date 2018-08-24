"""


Problem 5
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.


"""
print("""

***************

Programimiza hosgeldiniz....

***************

""")
i=1
while i<101:
    if i%3==0:
        print(i)
    i+=1
    continue
