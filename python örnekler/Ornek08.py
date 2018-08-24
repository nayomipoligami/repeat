# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: Kullanıcıdan bir sayı alarak, aldığı sayının pozitif ya da negatif olduğunu ekrana yazdıran
        algoritmayı tasarlayın.( Sıfır pozitif kabul edilecek)

    ALGORİTMA:
        Başla
        Yaz "Bir sayı girin: "
        Oku (sayi)
        Eğer
            (Sayı >= 0) Yaz "Girdiğiniz sayı pozitiftir."
            (Değilse) Yaz "Girdiğiniz sayı negatiftir."
        Dur
"""

sayi = input("Bir sayı girin:")
if (sayi >= 0):
    print "\n\tGirdiğiniz sayı pozitiftir."
else:
    print "\n\tGirdiğiniz sayı negatiftir."