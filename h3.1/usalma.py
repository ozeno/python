#-*- coding:utf-8 -*-

def usAl(sayi,us):
    x=1
    sonuc=1
    while x<=us:
        sonuc*=sayi
        x+=1
    return sonuc

sayi = int(input("Sayı girin: "))
us = int(input("Üs değerini girin: "))
print("Sonuç: {}".format(usAl(us=us,sayi=sayi)))