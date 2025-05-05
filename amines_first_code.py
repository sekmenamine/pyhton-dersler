import random

karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


parola_uzunlugu = int(input("Kaç karakterli bir parola oluşturmak istersin? "))
olusturulan_parola = ""
for i in range(parola_uzunlugu):
    secilen_karakter = random.choice(karakter)
    olusturulan_parola += secilen_karakter

print("işte senin güçlü parolan:" ,olusturulan_parola)  












