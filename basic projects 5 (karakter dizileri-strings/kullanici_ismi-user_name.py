# kullanıcı ismi sadece harf, rakam ve alt çizgi(_) içerebilir. Eğer kurallara uygunsa program "OK" yazar, değilse hatalı karakter yazdırılır.

karakterler=("abcdefghijklmnoprstuvyzwxq1234567890_")
isim=input("Kullanıcı adınızı giriniz: ")
Kontrol=True

for i in range(len(isim)):
    if isim[i] in karakterler:
        continue
    else:
        Kontrol=False
        print("geçersiz karakter: ",isim[i])
        break
if Kontrol:
    print("OK")