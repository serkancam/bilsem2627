"""
bir öğrenci fotokopi çektirmek için her gün kırtasiyeye gitmektedir.
fotokopici de fotokopi fiyatı/ödemesi çeşitli kurallara bağlıdır.
Bu kuralların yanında fotokopi masraflarıda sürekli değiştiğinden enflasyondan fotokopi fiyatıda etkilenmektedir. Öğrenci hem kurallara göre hem de o andaki fotokopi fiyatına göre ödemesini hesaplamak istemektedir.

* fotokopi fiyatını kullanıcı belirlesin(10  kuruş)
* haftanın pazartesi, salı ve çarşamba günleri fotokopi ücreti diğer günlere göre %20 daha ucuzdur(8 kuruş).
* çekim sayısı 100 kadar sabittir(yukarıdaki kurallar geçerlidir.)
* çekim sayısı 101 ile 300 arasında ise %5 indirim olur.
* çekim sayısı 301 ile 500 arasında ise %8 indirim olur.
* çekim sayısı 501 ve fazlası ise %10 indirim olur.
buna göre bu öğrencinin fotokopici de çektirdiği fotokopi fiyatını hesaplayan ve sonucu ekrana yazdıran algoritmayı geliştirerek python ile kodlayınız.
"""
fiyat=float(input("fiyat giriniz:"))
adet=int(input("adet giriniz:"))
gun=input("Hangi gün:")
indirim1=0
indirim2=0
if gun=="pazartesi" or gun=="salı" or gun=="çarşamba":
    indirim1=fiyat*0.2

if adet>=101 and adet<300:
    indirim2=fiyat*0.05
elif adet>300 and adet<500:
    indirim2=fiyat*0.08
elif adet>500:
    indirim2=fiyat*0.1

fiyat=fiyat-(indirim1+indirim2)

odeme=fiyat*adet
print(odeme)


