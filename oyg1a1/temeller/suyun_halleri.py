#Deniz seviyesinde sıcaklık değeri celcius birimi olarak girilen suyun kat, sıvı ve gaz olma durumlarını mantıksal olarak(True,False) belirten kodu yazınız.

sicaklik=float(input("suyun sıcaklığı:"))#35

kati_mi=sicaklik <=0 and sicaklik >= -273.15 #True/False
sivi_mi= sicaklik >0 and sicaklik <100 #True/False
gaz_mi=sicaklik >= 100  #True/False

print(kati_mi,sivi_mi,gaz_mi)