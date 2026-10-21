#Deniz seviyesinde sıcaklık değeri celcius birimi olarak girilen suyun kat, sıvı ve gaz olma durumlarını mantıksal olarak(True,False) belirten kodu yazınız.

sicaklik=float(input("suyun sıcaklığı:"))#35

kati_mi= sicaklik>=-273.15 and sicaklik<=0
sivi_mi= sicaklik>0 and sicaklik<100
gaz_mi= sicaklik>=100

print(kati_mi,sivi_mi,gaz_mi)