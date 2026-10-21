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
bu göre bu öğrencinin fotokopici de çektirdiği fotokopi fiyatını hesaplayan ve sonucu ekrana yazdıran algoritmayı geliştirerek pythpn ile kodlayınız.

"""
gun=input("gün giriniz:")
adet=int(input("fotokopi adedi:"))
fiyat=float(input("fotokopi fiyatı:"))
odeme=0
gun=gun.lower()
if gun=="pazartesi" or gun=="salı" or gun=="çarşamba":
    fiyat=fiyat*0.8
if adet>=101 and adet<300:
    fiyat=fiyat*0.95
elif adet>=301 and adet<5001:
    fiyat=fiyat*0.92
elif adet>500:
    fiyat=fiyat*0.9
odeme=adet*fiyat
print(odeme)


