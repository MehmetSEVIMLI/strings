# girilen yazıdaki en uzun kelimeyi ve uzunluğunu yazan programı yazınız.

yazi=input("Lütfen metni giriniz: ").split()

kelime=""
max=0

for k in yazi:
    if len(k)>max:
        kelime=k
        max=len(kelime)
print(kelime,max)