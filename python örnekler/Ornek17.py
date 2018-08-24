# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

from math import *
"""
    SORU: Yarıçapı ve yüksekliği verilen koninin hacmini hesaplayarak ekrana yazdıracak algoritmayı tasarlayın.

    ALGORİTMA:
        DISPLAY "Yarıçapı girin: "
        GET yaricap
        DISPLAY "Yüksekliği girin: "
        GET yukseklik
        alan = pi * r^2 /h
        DISPLAY "Alan = ",alan
"""
yaricap = input("Yarıçapı girin: ")
yukseklik = input("Yüksekliği girin: ")
alan = pi * pow(yaricap,2) / yukseklik
print "Alan = ",alan