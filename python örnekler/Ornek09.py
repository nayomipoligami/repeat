# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: Kullanıcıdan bir sayı alarak, aldığı sayının pozitif ya da negatif olduğunu ekrana yazdıran
        algoritmayı tasarlayın.( Eğer sayı 0 ise sıfır yazılacak)

    ALGORİTMA:
        Başla
        Yaz "Bir sayı girin: "
        Oku (sayi)
        Eğer (Sayı > 0 ) Yaz ("Girdiğiniz sayı pozitiftir.")
        Eğer (Sayı = 0 ) Yaz ("Girdiğiniz sayı sıfırdır.")
        Eğer (Sayı < 0 ) Yaz ("Girdiğiniz sayı negatiftir.")
        Dur
"""
sayi = input("Bir sayı giriniz: ")
if sayi > 0 : print "\n\tGirdiğiniz sayı pozitiftir."
if sayi == 0 : print "\n\tGirdiğiniz sayı sıfırdır."
if sayi < 0 : print "\n\tGirdiğiniz sayı negatiftir."

"""
    Çok seçenekli koşul yapısı kullanılarak oluşturulan algoritma:
        Başla
        Yaz "Bir sayı girin: "
        Oku (sayi)
        Eğer
            (sayi > 0 ) Yaz "Girdiğiniz sayı pozitiftir."
            (sayi < 0 ) Yaz "Girdiğiniz sayı negatiftir."
            (Değilse) Yaz "Girdiğiniz sayı sıfırdır."
        Dur
"""
print "\n\n------Çok Seçenekli Algoritma tasarımı---------\n"

if (sayi > 0):
    print "\tGirdiğiniz sayı pozitiftir."
elif (sayi < 0):
    print "\tGirdiğiniz sayı negatiftir."
else:
    print "\tGirdiğiniz sayı sıfırdır."

"""
    İç içe koşul yapısı kullanılarak oluşturulan algoritma:
        Başla
        Yaz "Bir sayı girin:"
        Oku (sayi)
        Eğer
            (sayi > 0) Yaz "Girdiğiniz sayı pozitiftir."
            (Değilse)
                Eğer (Sayı < 0) Yaz "Girdiğiniz sayı negatiftir."
                (Değilse) Yaz "Girdiğiniz sayı pozitiftir."
        Dur
"""
print "\n\n-----İç içe koşul yapısı ile -----\n"
if (sayi > 0):
    print "\tGirdiğiniz sayı pozitiftir."
else:
    if (sayi < 0):
        print "\tGirdiğiniz sayı negatiftir."
    else:
        print "\tGirdiğiniz sayı sıfırdır."