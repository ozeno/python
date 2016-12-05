#-*- coding: utf-8 -*-
rakamlar = "123456789" # Değişkenin değeri karakter dizisi olduğu için her değeri tek tek ele alıp işleyecektir.

for n in rakamlar:
    print(int(n)*2,end=" ")  # Karakter tipindeki değeri int() fonksiyonu ile tamsayıya çevirip 2 ile çarptık.
    
print()  # Bir satır alta indik. Güzel görünüm açısından.
for n in rakamlar:
    print(n*2,end=" ") # Karakter tipindeki değeri *2 kullanarak iki kere yazdırdı.
    
# end parametresi print fonksiyonunun işini yaptıktan sonra ne yazacağını belirtir. Varsayılan olarak \n (new line) dir.
#Yani yazdıktan sonra bir alt satıra iner. Burda tek boşluk kullanarak yazdırdıktan sonra alt satıra inmektense bir boşluk
# bırakmasını sağladık.
