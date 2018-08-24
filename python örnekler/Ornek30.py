# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: 1'den 10'a kadar olan sayıların, yanlarına Tek/Çift diye yazdıran algoritmayı tasarlayın.

    ALGORİTMA:
        FOR (X=1 TO 10 STEP 1)
            IF (X MOD 2 = 0) THEN
                DISPLAY "X - Çift"
            ELSE
                DISPLAY "X - Tek"
            ENDIF
        ENDFOR
"""
for sayi in range(1,11,1):
    if sayi % 2 == 0:
        print sayi," - Çift"
    else:
        print sayi," - Tek"