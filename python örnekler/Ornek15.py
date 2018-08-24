# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: Tabanı ve yüksekliği verilen bir üçgenin alanını hesaplayarak ekrana yazdıran algoritmayı tasarlayın.

    ALGORİTMA:
        DISPLAY "Taban uzunluğunu girin: "
        GET taban
        DISPLAY "Yüksekliği girin: "
        GET yukseklik
        alan = (taban*h) / 2.0
        DISPLAY "Alan = ",alan
"""

taban = input("Taban uzunluğu girin: ")
yukseklik = input("Yüksekliği girin: ")
alan= (taban*yukseklik)/2.0
print "Alan = ",alan