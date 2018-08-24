# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: İnç cinsinden verilen uzunluğu santimetre cinsine çevirerek hesaplayan algoritmayı tasarlayın.

    ALGORİTMA:
        DISPLAY "Uzunluğu (inç) giriniz: "
        GET incUzunluk
        incTocm = incUzunluk * 2.54
        DISPLAY "Uzunluğun (cm) karşılığı = ",incTocm
"""
incUzunluk =input("Uzunluğu (inç) giriniz: ")
incTocm = incUzunluk * 2.54
print "Uzunluğun (cm) karşılığı = ",incTocm," cm"