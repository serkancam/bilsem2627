# parker_sure.py

kutupyaricap=6357
ekvatoryaricap=6379
pi=3.14
hiz=150
##ekvatoru dolaşma süresi(sn)##
ekvator_cevre=2*pi*ekvatoryaricap
ekvator_sure=ekvator_cevre/hiz
print("ekvator süresi:",ekvator_sure,"saniye")
##kutup dolaşma süresi(sn)##
kutup_cevre=2*pi*kutupyaricap
kutup_sure=kutup_cevre/hiz
print(f"kutup süresi:{kutup_sure} saniye") 

"""
* bir aritmetik işleme giren sayılardan bir tanesi bile ondalıklı sayı(float) ise sonuç ondalıklı çıkar. 
* bir aritmetik işlemde / işlemi varsa sonuç ondalıklı çıkar. 
* Geri kalan aritmetik işlemlerde sonuç tam sayı(integer) çıkar.
"""
#hesaplanan kutup ve ekvator dolanma sürelerini  dakika:saniye şeklinde dönüştürüne kodu yazınız

#kutup
kutup_sure=int(kutup_sure)
kutup_dakika=kutup_sure//60
kutup_saniye=kutup_sure%60
print(f"{kutup_dakika} dakika:{kutup_saniye} saniye")#"x dakika y saniye"

#ekvator
ekvator_sure=int(ekvator_sure)
ekvator_dakika=ekvator_sure//60
ekvator_saniye=ekvator_sure%60
print(f"{ekvator_dakika} dakika:{ekvator_saniye} saniye")#"x dakika y saniye"


      



