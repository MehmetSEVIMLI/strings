# Girilen yazı palindorm ise EVET, değilse HAYIR yazan programı yazınız.
#yazıdaki boşluklar hesaba katılmayacak.
#palindrom : soldan sağa ve sağdan sola okunduğunda aynı olan yazıdır.

s=input()
t=""
for i in range(len(s)):
    if s[i] !=" ":
        t+=s[i]
        
kontrol=True

for i in range(len(t)//2):
    if t[i].lower() != t[len(t)-1-i].lower():
        kontrol=False
        break
if kontrol:
    print("EVET")
else:
    print("HAYIR")