# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: Kullanıcının girdiği sayıları toplayan bir algoritma tasarlayın. Algoritma, kullanıcını 0(sıfır) girene
        kadar girdiği sayıları alıp toplasın ve kullanıcı 0(sıfır) girdiğinde kullanıcıdan sayı alma işlemini kesip,
        girilen sayıların toplamını ekrana yazdırsın.

    ALGORİTMA:

"""
toplam = 0
while(True):
    sayi = input("Bir sayi girin: ")
    if sayi == 0: break
    toplam += sayi


print "Sayıların toplamı = ",toplam
