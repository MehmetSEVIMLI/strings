# programa birinci şehir ismi girilir ve daha sonraikinci şehir ismi girilir.
# Birinci şehrin son harfi ile ikinci şehrin ilk harfi aynı ise yei şehir okumaya devam edilir ve son girilen şehir ikinci şehir olur.
#böylece kural sağlandığı sürece şehir ismi girilmeye devam edilir. Kural bozulduğu zaman en son girilen şehir, yani kuralı bozanşehir yazılır.

# sehir1=input("1.Şehri giriniz: ")
# print(sehir1[-1])
# while True:
#     sehir2=input("2. Şehri giriniz: ")
#     if sehir2=="q":
#         break
#     elif sehir1[-1]==sehir2[0]:
#         sehir1=sehir2
#     elif sehir1[-1]!=sehir2[-1]:
#         print("son harf: ", sehir1[-1])
#         print("yanlış giriş : ",sehir2, sehir2[0])
#         break


##################

sehir1=input("1.Şehri giriniz: ")
sehir2=input("2.Şehri giriniz: ")

while sehir1[-1]==sehir2[0]:
    sehir1=sehir2
    sehir2=input("2.Şehri giriniz: ")
    
print(sehir2)