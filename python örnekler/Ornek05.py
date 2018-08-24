# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: Kullanıcıdan bir sayı alıp, 1'den başlayarak kullanıcıdan aldığı sayıya kadar bir arttırarak ekrana
        yazdıran algoritmayı tasarlayın.

    ALGORİTMA:
        Başla
        SAYAC = 0, TOPLAM = 0
        Oku SAYI
        Eğer SAYAC >= SAYI, 8. adıma git
        TOPLAM = TOPLAM + SAYAC
        SAYAC = SAYAC + 1
        4. adıma git
        Yaz TOPLAM
        Dur
"""
sayi  = input("Bir sayı giriniz: ")
sayac = 0
toplam = 0
while(sayac <= sayi):
    toplam += sayac
    sayac += 1

print toplam