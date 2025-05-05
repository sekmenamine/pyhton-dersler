birinci_sayı = int(input("Birinci sayıyı giriniz: "))
ikinci_sayı = int(input("İkinci sayıyı giriniz: "))

işlem = input("Yapmak istediğiniz işlemi giriniz (+, -, *, /): ")

if işlem == "+":
    sonuç = birinci_sayı + ikinci_sayı

elif işlem == "-":
    sonuç = birinci_sayı - ikinci_sayı

elif işlem == "*":
    sonuç = birinci_sayı * ikinci_sayı   

elif işlem == "/":
    if ikinci_sayı == 0:
        sonuç = "Bölme işlemi için ikinci sayı sıfır olamaz."
    else:
        sonuç = birinci_sayı / ikinci_sayı

else:
    sonuç = "Geçersiz işlem. Lütfen +, -, * veya / giriniz."

print("Sonuç:", sonuç)
# Bu kod, kullanıcıdan iki sayı alır ve belirtilen işlemi gerçekleştirir.