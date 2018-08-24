# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: Kullanıcıdan yaşını alıp, girilen değer 18'e eşitse ya da 18'den büyükse ekrana "Reşitsiniz"
         girilen değer 18'de küçükse "Reşit değilsiniz" yazdıran algoritmayı tasarlayın.

    ALGORİTMA:
        Başla
        Oku "Yaşınız?" (yas)
        Eğer
            (yas >= 18) yaz "Reşitsiniz"
            (Değilse) yaz "Reşit değilsiniz"
        Dur
"""

yas = input("Yaşınız ? ")
if (int(yas) >= 18):

    print ("Reşitsiniz.")
else:
    print ("Reşit değilsiniz.")
