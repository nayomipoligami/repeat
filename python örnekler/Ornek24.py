# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: Girilen iki sayıyı büyüklük, küçüklük, eşitlik bakımından karşılaştırıp, ekrana yazan algoritmayı tasarlayın.

    ALGORİTMA:
        DISPLAY "Sayı1 = "
        GET sayi1
        DISPLAY "Sayı2 = "
        GET sayi2
        IF sayi1 > sayi2 THEN
            DISPLAY "sayi1 > sayi2"
        ELSEIF sayi1 < sayi2 THEN
            DISPLAY "sayi1 < sayi2"
        ELSE
            DISPLAY "sayi1 = sayi2"
        ENDIF
"""
sayi1 = input("Sayı1 = ")
sayi2 = input("Sayı2 = ")
if sayi1 > sayi2 :
    print "\tsayi1 > sayi2"
elif sayi1 < sayi2:
    print "\tsayi1 < sayi2"
else:
    print "\tsayi1 = sayi2"