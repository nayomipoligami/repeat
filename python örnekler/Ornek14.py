# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: A ve B kenarları verilen bir dikdörtgenin çevresini ve alanını hesaplayarak ekrana yazdıran
        algoritmayı tasarlayın

    ALGORİTMA:
        DISPLAY "A kenarının uzunluğunu girin: "
        GET a
        DISPLAY "B kenarının uzunluğunu girin: "
        GET b
        cevre = 2*(a+b)
        alan = a*b
        DISPLAY "Dikdörtgenin çevresi = ",cevre
        DISPLAY "Dikdörtgenin alanı = ",alan
"""

a = input("A kenarının uzunluğunu girin: ")
b = input("B kenarının uzunluğunu girin: ")
cevre = 2*(a+b)
alan = a*b

print "Çevre = ",cevre
print "Alan = ",alan
