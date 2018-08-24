# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: Klavyeden katsayıları verilen birinci derecede denklemin köklerini hesaplayarak ekrana basan algoritmayı
        tasarlayın.

    a*x + b = 0 denklemin kökü x = -b/a 'dır.

    ALGORİTMA:
        DISPLAY "X'in katsayısını(a) girin: "
        GET a
        DISPLAY "b yi girin: "
        GET b
        x = -1 * b / a
        DISPLAY "Denklemin kökü = ",x
"""

a = input("X'in katsayısını (a) girin: ")
b = input("b yi girin: ")
x = -1 * b / round(a,1)

print "Denklemin kökü = ",round(x,2)