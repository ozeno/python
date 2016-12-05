
print("""
Yapmak istediğiniz işlemi seçin:
1) Toplama  (+)
2) Çıkarma  (-)
3) Çarpma   (*)
4) Bölme    (/)
""")

while True:
    islem = int(input("İşlem numarası(1-4): "))
    if islem in [1,2,3,4]:
        ilkSayi = int(input("  İlk sayı: "))
        ikinciSayi = int(input("  İkinci sayı: "))
        if islem is 1:
            print("  Sonu ç: {}".format(ilkSayi+ikinciSayi))
            break
        elif islem is 2:
            print("  Sonuç: {}".format(ilkSayi-ikinciSayi))
			
        elif islem is 3:
            print("  Sonuç: {}".format(ilkSayi*ikinciSayi))
            break
        elif islem is 4:
            print("  Sonuç: {}".format(ilkSayi/ikinciSayi))
            break
    else:
        print("Hatalı işlem!")