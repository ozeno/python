#-*- coding:utf-8 -*-
metin = input("Metin giriniz: ")
anahtar = int(input("Anahtar giriniz(sayı): "))

for i in metin:
	print(chr(ord(i)+anahtar),end="")

# Bu program girilen metindeki her karakteri anahtar değeri kadar artırır. Yani 2 anahtarı ile 'a' harfi 'c' harfi
# olacaktır. Yalnız ascii tablosu kullanıldığı için bazen harf yerine sayı/alfanumerik olmayan karakterler de görebilirsiniz.