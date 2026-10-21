# karsilastirma_mantik_operatorleri.py
#dersten geçme kuralı
#kullanıcıdan 1. not ve 2. not bilgisini alarak(float) aşağıdaki kurala göre ders geçme durumunu tespit ediniz. ders geçme durmunu durum adlı bir değişkene aktarınız ve ekrana yazdırınız.
# ders geçmek için iki sınavın ortalaması 50 veya üstünde olmalı veya 2. sınav 70 veya üzerinde bir nota sahip olmalıdır
#sonuç ders geçme durumu olumlu ise True değilse False olmalaıdır.

s1=float(input("sınav1:"))
s2=float(input("sınav2:"))

ort=(s1+s2)/2
# durum= ((s1+s2)/2) >=50 or s2 >= 70

# d1= ((s1+s2)/2) >=50
# d2=s2 >= 70
# d=d1 or d2
durum = ort>=50 or s2>=70
print(durum)