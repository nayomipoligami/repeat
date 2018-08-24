# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: Klavyeden kütlesi ve molekül ağırlığı girilen maddenin mol sayısını hesaplayarak ekrana yazan algoritmayı
        tasarlayın.

    ALGORİTMA:
        DISPLAY "Kütleyi giriniz: "
        GET kutle
        DISPLAY "Molekül ağırlığını girin: "
        GET mAgirligi
        mol = kutle / mAgirligi
        DISPLAY "Mol = ",mol
"""
kutle = input("Kütleyi girin: ")
mAgirligi = input("Molekül ağırlığını girin: ")
mol = kutle / round(mAgirligi,1)

print "Mol = ",round(mol,2)
