#kontrol yapıları
"""
if elif else

== != < > <= >= 
and or not 
in is ...

"""


sicaklik=float(input("suyun sıcaklığı:"))#35

if sicaklik>=-273.15 and sicaklik<0:
    print("katı")
elif sicaklik>=0 and sicaklik<100:
    print("sıvı")
elif sicaklik>=100:
    print("gaz")
else:
    print("Evrende bu kadar düşük ısı olamaz.")





