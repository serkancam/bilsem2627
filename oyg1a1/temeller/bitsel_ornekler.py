#s1 sayısını 2 sağa kaydırın ve sonucu ekrana yazıdırın

s1=12
s2=25
print(s1>>2)
#s2 sayısını 2 sola kaydırın

print(s2<<2)

#s1 ve s2 sayılarını bitsel olarka and(&) işlemine sokun ve ekrana yazdırın

print(s1&s2)

#s1 ve s2 saylarını bitsel XOR(^) işlemine tabi tutarak s3 değişkenine aktarın ve s3 ekrana yazdırın
s3=s1^s2
print(s3)
#s3 sayısnın not(~) ile elde edip sonuca 1 ekleyin ve s4 değişkenine aktararak ekrana s4 değerini yazdırınız.
s4=~s3+1#sayının negatif halini verir
print(s4)

#s4 değişkenini 27 sayısı ile bitsel or(|) işlemine tabi tutup sonucu s5 değişkenine aktarınız.
s5=s4|27

# oluşan bütün değişkenlerin toplamını ekrana yazdırınız.
toplam=s1+s2+s3+s4+s5
print(toplam)





