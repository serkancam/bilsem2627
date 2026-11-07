buyuk = int(input("büyük sayı:"))
kucuk = int(input("küçük sayı:"))

# TODO: Aşağıdaki yorum satırlarını silip kendi while döngünü buraya yaz!

if not(buyuk>kucuk):
    #buyuk,kucuk=kucuk,buyuk #swap
    temp=kucuk
    kucuk=buyuk
    buyuk=temp


while kucuk!=0:
    kalan = buyuk%kucuk
    buyuk = kucuk
    kucuk = kalan

print("EBOB değeri:", buyuk)