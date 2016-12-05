baslangic = int(input("Başlangıç değeri girin: "))
bitis = int(input("Bitiş değeri girin: "))
artisMiktari = int(input("Artış miktarını girin: "))
while baslangic<=bitis:
    print("Yeni değer: {}".format(baslangic))
	baslangic+=artisMiktari  
    if baslangic>=bitis:
        print("Bitti!")
        break