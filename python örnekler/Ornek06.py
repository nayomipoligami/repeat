# coding=utf-8
__author__ = 'Sercan GEZER'
# !/usr/bin/env python
"""
    SORU: Kişiye adını soracak, daha sonra da adını kullanarak cinsiyet unvanını(Bay/Bayan) soracak ve
        kullanıcının cinsiyet unvanıyla adını birleştirerek ekrana "Esenlikler, Sayın X Bey/Hanım" yazdıran
        algoritmayı tasarlayın.

    ALGORİTMA:
        Başla
        Yaz "Adınızı girin: "
        Oku (ad)
        Yaz "Sayın " + ad + ", lütfen cinsiyet ünvanınızı Bey / Hanım girin: "
        Oku (unvan)
        Yaz "Esenlikler, Sayın " + ad + " " + unvan
        Dur
"""

ad = raw_input("Adınızı girin: ")
unvan = raw_input("Lütfen cinsiyet unvanınızı Bey/Hanım girin: ")
print "Esenlikler, Sayın ",ad,unvan