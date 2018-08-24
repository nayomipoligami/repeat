# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: Girilen sayıyı, girilen sayının 2 katı kadar ekrana yazdıran algoritmayı tasarlayın.

    ALGORİTMA:
        DISPLAY "Sayi = "
        GET sayi
        FOR (x = 1 TO sayi * 2 STEP 1)
            DISPLAY sayi
        ENDFOR
"""
sayi = input("Sayı = ")
for i in range(0,sayi*2,1):
    print sayi
    i += 1