# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: Kullanıcıdan 100 adet sayı alarak, bu sayıların toplamını ekrana yazdıran algoritmayı tasarlayın.

    ALGORİTMA:
        Başla
        Toplam = 0
        Sayac ( 1 to 100 step 1)
        Yaz "Bir sayi girin: "
        Oku (sayi)
        Toplam = toplam + sayi
        SayacSonu
        Yaz Toplam
        Dur
"""
toplam = 0
for i in range(0,100,1):
    sayi = input("Bir sayı giriniz: ")
    toplam += sayi
    i += 1

print toplam
