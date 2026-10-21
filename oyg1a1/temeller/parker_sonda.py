kutup_r=6357
ekvator_r=6379
pi=3.14
parker_hiz1=150#km/sn
parker_hiz2=192

####ekvatoru kaç saniyede dolanır####
ekvator_cevre=2*pi*ekvator_r#km
ekvator_suresi=ekvator_cevre/parker_hiz1
print(f"ekvatoru parker {ekvator_suresi} saniyede dolanır")

####kutupları kaç saniyede dolanır####
kutup_cevresi=2*pi*kutup_r
kutup_suresi=kutup_cevresi/parker_hiz2
print(f"kutupları parker {kutup_suresi} saniyede dolanır")

###kutup etrafını kaç dakika:saniyede dolanır####

kutup_suresi=int(kutup_suresi)

kutup_dakika=kutup_suresi//60
kutup_saniye=kutup_suresi%60
#2 dakika 17 saniye
print(f"{kutup_dakika} dakika {kutup_saniye} saniye")

###Ekvator etrafını kaç dakika:saniyede dolanır####

ekvator_suresi=int(ekvator_suresi)

ekvator_dakika=ekvator_suresi//60
ekvator_saniye=ekvator_suresi%60
#2 dakika 17 saniye
print(f"{ekvator_dakika} dakika {ekvator_saniye} saniye")















"""
operatörler

Aritmetiksel Operatör: 
Programlama dillerinde aritmetiksel işlemlerin yapılabilmesi için kullanılan operatörlerdir. (+, -, *, /, **, %,//,= gibi)

Mantıksal Operatör: Birden çok sayıdaki mantıksal ifadeyi birbirine bağlayarak yeni ifadeler oluşturmak için kullanılan bağlaçlardır. Önermeler mantığındaki kurallara göre değer alırlar. Örneğin AND operatörü ile bağlanan ifadelerden oluşan bir koşul ancak bağlı ifadelerin tamamı doğru ise doğru değerini alabilir. Diğer bütün durumlarda yanlıştır. Benzer şekilde OR operatörü ile bağlanan ifadelerden oluşan bir koşul ancak bağlı ifadelerin tamamı yanlış ise yanlış değerini alır. Diğer bütün durumlarda doğrudur.

Karşılaştırma Operatörü: Programlama dillerinde aynı veri türlerine sahip değişkenlerin ve/veya sabitlerin değerlerinin karşılaştırması için kullanılan operatörlerdir (<, >, ==, gibi). 
"""