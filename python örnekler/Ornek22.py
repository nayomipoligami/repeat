# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python

"""
    SORU: 100 üzerinden 70 başarı notuyla, ekrana girilen nota göre kullanıcıya başarılı olup olmadığını gösteren
        algoritmayı tasarlayın.

    ALGORİTMA:
        DISPLAY "Puan giriniz: "
        GET puan
        IF puan >= 70 THEN
            DISPLAY "Başarılı"
        ELSE
            DISPLAY "Başarısız"
        ENDIF
"""
puan = input("Puan giriniz: ")

if puan <= 100:
    if puan >= 70:
        print "\tBaşarılı"
    else:
        print "\tBaşarısız"
else:
    print "\tGirdiğiniz puan 0-100 arasında olmalıdır.".upper()