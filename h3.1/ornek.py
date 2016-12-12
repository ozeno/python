# Bu örnek program kelimenin içinde harf olup olmadığını kontrol eder.

def kontrol():
    kelime = "deneme"
    harf = "c"
    if harf in kelime:
        return True
    else:
        return False

if kontrol():
    print("Var.")
else:
    print("Yok.")
