# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: Girilen iki sayıdan, ilkinin ikinci sayıya tam bölünüp bölünmediğini hesaplayarak ekrana yazan algoritmayı
        tasarlayın.

    ALGORİTMA:
        DISPLAY "Sayı1 = "
        GET sayi1
        DISPLAY "Sayı2 = "
        GET sayi2
        IF sayi1 MOD sayi2 = 0 THEN
            DISPLAY "Sayi1, sayi2 ye tam bölünür."
        ELSE
            DISPLAY "Sayi1, sayi2 ye tam bölünmez."
        ENDIF
"""
sayi1 = input("Sayı1 = ")
sayi2 = input("Sayı2 = ")
if sayi1 % sayi2 == 0:
    print sayi1,", ",sayi2," ye tam bölünür."
else:
    print sayi1,", ",sayi2," ye tam bölünmez."