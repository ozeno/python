#-*- coding: utf-8 -*-

sayi = int(input("Sayı giriniz: "))


def faktoriyel(deger):
    i=1
    sonuc=1
    while i<=deger:
        sonuc*=i   # sonuc = sonuc * i
        i+=1
    return sonuc
print(faktoriyel(sayi))
