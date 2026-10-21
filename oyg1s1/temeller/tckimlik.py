"""
“T.C. kimlik numarası doğrulama algoritması nasıl yapılmaktadır?”

1. T.C. kimlik numaralarının 1.,3., 5., 7. ve 9. hanelerinin toplamının 7 katından 2., 4., 6. ve 8. hanelerinin toplamı çıkarılır; elde edilen sonucun birler basamağı 10. rakamı verir.

2. T.C. kimlik numarasının ilk 10 rakamın toplamının birler basamağı 11. rakamı vermektedir.

"""

tc_9=input("TC ilk 9 hanesini giriniz: ")
toplam1=0
toplam2=0
for i in range(9):    
    if(i%2==0):
        toplam1=toplam1+int(tc_9[i])
    else:
        toplam2=toplam2+int(tc_9[i])

b10=(7*toplam1-toplam2)%10
b11=(toplam1+toplam2+b10)%10
print(b10,b11)


# b1=int(tc_9[0])
# b2=int(tc_9[1])
# b3=int(tc_9[2])
# b4=int(tc_9[3])
# b5=int(tc_9[4])
# b6=int(tc_9[5])
# b7=int(tc_9[6])
# b8=int(tc_9[7])
# b9=int(tc_9[8])

# b10=(7*(b1+b3+b5+b7+b9)-(b2+b4+b6+b8))%10
# b11=(b1+b2+b3+b4+b5+b6+b7+b8+b9+b10)%10
# print(b10,b11)

