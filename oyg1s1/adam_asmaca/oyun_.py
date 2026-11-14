import os
import time
import random

#1-
dosya=open(file="./adam_asmaca/ulkeler.txt",mode="r",encoding="utf-8")
satirlar=dosya.readlines()
dosya.close()# her kaynak(kamera,mikrofon dosya vb.) kullınıldıkran sonra hemen kapatılır.
print(satirlar)
#2-
soru=random.choice(satirlar)
soru=soru.strip().lower()
print(soru)
#3-
hak=5
#4-
bilinenler=list()#boş liste
#5-
soylenenler=[]#boş liste
#6-

while hak>=0: #hak != 0
    os.system("clear")
    print(f"hak={hak}")#6.1-
    print(f"söylenenler={soylenenler}")#6.2-
    #6.3-
    for harf in soru:
        if harf in bilinenler:
            print(harf,end=" ")
        else:
            print("_",end=" ")
    hr=input("harf:")#6.4-
    if hr in soylenenler:#6.5
        print("söylenmeyen harf giriniz:")
        time.sleep(1)
        continue
    if hr in soru:#6.6-
        bilinenler.append(hr)
      
    else:
        hak=hak-1
    soylenenler.append(hr)#6.7.
    if len(bilinenler)==len(set(soru)):#6.8-
        os.system("clear")
        print(f"Tebrikler, cevap :{soru}")
        break
if hak==0:
    print(f"Kaybettiniz! cevap *{soru}* oalcaktır")
