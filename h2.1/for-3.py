# Pangram
metin1 = "the quick brown fox jumps over the lazy dog"
metin2 = "pijamalı hasta yağız şoföre çabucak güvendi"
for deger in metin1:
    if not deger in metin2:
        print("Farklı harfler: {}".format(deger))

