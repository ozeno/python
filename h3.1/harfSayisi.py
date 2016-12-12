# Bu programdaki harfSayisi fonksiyonu parametre olarak aldığı metindeki karakter sayısını hesaplar.
# Bunun yerine len() fonksiyonu da kullanılabilirdi. Fakat len() fonksiyonunda boşluk(" ") karakteri
# de sayılacaktır. Bu programda for döngüsünün içindeki if bloğunda boşluk karakterine rastlandığında
# atlaması istenmiştir.
metin= input("Metin: ")

def harfSayisi(deger):
    toplam=0
    for i in deger:
        if i==" ":
            continue
        else:
            toplam+=1
    return toplam

print(harfSayisi(deger=metin))