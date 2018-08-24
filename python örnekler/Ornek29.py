# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: 1'den 10'a kadar sayıların küplerini alarak ekrana yazdıran algoritmayı tasarlayın.

    ALGORİTMA:
        FOR (X=1 TO 10 STEP 1)
            DISPLAY x*x*x
        ENDFOR
"""
for sayi in range(1,11,1):
    print sayi," ",(sayi*sayi*sayi)
