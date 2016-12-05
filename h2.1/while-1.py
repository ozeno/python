#-*- coding: iso-8859-9 -*-

# Kullanıcıdan alınan başlangıçtan bitiş değerine kadar yine kullanıcıdan alınan artış miktarı kadar artarak giden
# ve bunları ekrana yazdıran kod.

baslangic = int(input("Başlangıç değeri girin: "))
bitis = int(input("Bitiş değeri girin: "))
artisMiktari = int(input("Artış miktarını girin: "))
while baslangic<=bitis:
	print("Değer: {}".format(baslangic))
	baslangic+=artisMiktari
    
