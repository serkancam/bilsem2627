"""1. adım"""
import random
import os
import time
dosya=open(file="./adam_asmaca/ulkeler.txt",mode="r",encoding="utf-8")
sorular=dosya.readlines()
#her kaynak işi bitince kapatılır
#kaynakalra örnek: dosya, kamera, mikrofon, yazıcı...
dosya.close()
print(sorular)
"""2 ve 3. adım"""
soru=random.choice(sorular).strip().lower()
# soru=soru.strip()
print(soru)
"""4. adım"""
hak=6
"""5. adım"""
soylenenler=list()#boş liste
"""6. adım"""
bilinenler=[]#boş liste
"""7. adım"""
os.system("clear")
while hak != 0:# hak sıfırdan faraklı iken
    print(f"hak:{hak}")#7.1
    print(f"söylenenler:{soylenenler}")#7.2
    t=0
    for harf in soru:#7.3
        if harf in bilinenler:
            print(harf,end=" ")
        else:
            print("_",end=" ")
            t=t+1
    if t==0:
        os.system("clear")
        print("Tebrikler")
        break

    h=input("harf:").lower()#7.4
    if h in soylenenler:
        print("söylenmyen harf gir:")
        time.sleep(1)
        os.system("clear")
        continue
    if h in soru:#7.5
        bilinenler.append(h)
    else:
        hak=hak-1
    soylenenler.append(h)#7.6
    os.system("clear")


if hak==0:
    print(f"Kaybettiniz. cevap:{soru}")
    exit()
