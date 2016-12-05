sesliHarfler = "aeıioöuü"
sessizHarfler = "bcçdfgğhjklmnprsştvyz"
sesliHarfSayisi=sessizHarfSayisi=0
kelime = input("Kelime girin: ")
for i in kelime:
    if i in sesliHarfler:
        sesliHarfSayisi+=1  #sesliHarfSayisi=sesliHarfSayisi+1
    else:
        sessizHarfSayisi+=1

print("Sesli harf sayısı: " + str(sesliHarfSayisi) + " Sessiz harf: " + str(sessizHarfSayisi))