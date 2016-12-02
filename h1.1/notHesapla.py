#!/usr/bin/python3
"""
Bu kısa betik önce öğrencinin adını alıyor. Sonra vize ve final notlarını alıyor. input fonksiyonu, varsayılan olarak girdiyi string tipinde aldığı için işlem yapabilmek adına bunları float tipine çeviriyor.
Not: Tip değişimleri bahsedildiği gibi 'tip(değişken)' söz dizimini kullanılarak yapılıyor.
Sonra ortalamayı hesaplayıp ortalamaya göre karar yapılarına giriyor ve ortalamanın olduğu aralıktaki harf notunu yazdırıyor.
"""

ogrenciAdi = input("Öğrencinin adını giriniz: ")     
vizeNotu = float(input("Vize notunu giriniz: "))    
finalNotu = float(input("Final notunu giriniz: "))   
ortalama = vizeNotu*0.4 + finalNotu*0.6              
print(ogrenciAdi + " adlı öğrencinin ortalaması =" + str(ortalama))
if ortalama>=87:
    print("Harf notu: AA")
elif ortalama>=81 and ortalama<87:
    print("Harf notu: BA")
elif ortalama>=74 and ortalama<81:
    print("Harf notu: BB")
elif ortalama>=67 and ortalama<74:
    print("Harf notu: CB")
elif ortalama>=60 and ortalama<67:
    print("Harf notu: CC")
elif ortalama>=53 and ortalama<60:
    print("Harf notu: DC")
elif ortalama>=46 and ortalama<53:
    print("Harf notu: DD")
elif ortalama>=39 and ortalama<46:
    print("Harf notu: FD")
else:
    print("Harf notu: FF")
