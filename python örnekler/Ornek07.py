# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU:Kullanıcıdan adını alıp, eğer kullanıcının adındaki karakter sayısı 7'den büyükse
        ekrana "Uzun bir ada sahipsiniz." yazdıran algoritmayı tasarlayın.

    ALGORİTMA:
        Başla
        Yaz "Adınızı girin: "
        Oku (ad)
        Yaz (ad)
        Eğer
            (ad) değerinin uzunluğun 7 karakterden büyükse ekrana "uzun bir ada sahipsiniz."
        Dur
"""
ad = raw_input("Adınızı girin:")
if (len(ad)>7):
    print "\tUzun bir ada sahipsiniz."