# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: Fahrenayt cinsinden verilen sıcaklığın Santigrad cinsine çevirerek hesaplayan algoritmayı tasarlayın.

    ALGORİTMA:
        DISPLAY "Sıcaklığı Fahrenayt cinsinden giriniz: "
        GET fsicaklik
        fahToSant = ( fsicaklik - 32 ) / 1.8
        DISPLAY fsicaklik," Fahrenayt = ",fahToSant," Santigrad"
"""
fsicaklik = input("Sıcaklığı Fahrenayt cinsinden giriniz: ")
fahToSant = (fsicaklik - 32) / 1.8
print fsicaklik," Fahrenayt = ",round(fahToSant,1)," Santigrad a eşittir."

#round(sayi,Kac basamak gosterileceği)