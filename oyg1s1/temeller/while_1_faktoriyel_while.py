# ==============================================================================
# KONU 1: FAKTÖRİYEL HESAPLAMA (Adım Adım While Döngüsüne Geçiş)
# ==============================================================================
#
# 1. TANIM VE KÂĞIT-KALEM İLE ELLE ÇÖZÜM:
# Bir sayının faktöriyeli, 1'den o sayıya kadar olan tüm tam sayıların çarpımıdır.
# Matematikte "!" işareti ile gösterilir.
#
# Örnek olarak 4! (4 Faktöriyel) işlemini kağıt üzerinde adım adım yapalım:
# Başlangıçta elimizde çarpma işleminin etkisiz elemanı olan 1 var (Sonuç = 1).
#
# 1. Adım: Sonuç = 1 * 1  -> Sonuç = 1 oldu.
# 2. Adım: Sonuç = 1 * 2  -> Sonuç = 2 oldu.
# 3. Adım: Sonuç = 2 * 3  -> Sonuç = 6 oldu.
# 4. Adım: Sonuç = 6 * 4  -> Sonuç = 24 oldu.
#
# Gördüğünüz gibi her adımda bir önceki sonucu sıradaki sayıyla çarpıyoruz!
# ==============================================================================

print("--- 1. BÖLÜM: DÖNGÜSÜZ (ELLE ADIM ADIM) FAKTÖRİYEL ---")

# 4 sayısının faktöriyelini döngü KULLANMADAN hesaplayalım:
sonuc = 1  # Çarpma işleminde etkisiz eleman 1 olduğu için 1 ile başlıyoruz.
carpan = 1 # Çarpmaya 1'den başlıyoruz.

# 1. Adım (Çarpan: 1)
sonuc = sonuc * carpan
print("1. Adım -> Çarpan:", carpan, "| Güncel Sonuç:", sonuc)
carpan = carpan + 1  # Sıradaki sayıya geç (2 oldu)

# 2. Adım (Çarpan: 2)
sonuc = sonuc * carpan
print("2. Adım -> Çarpan:", carpan, "| Güncel Sonuç:", sonuc)
carpan = carpan + 1  # Sıradaki sayıya geç (3 oldu)

# 3. Adım (Çarpan: 3)
sonuc = sonuc * carpan
print("3. Adım -> Çarpan:", carpan, "| Güncel Sonuç:", sonuc)
carpan = carpan + 1  # Sıradaki sayıya geç (4 oldu)

# 4. Adım (Çarpan: 4)
sonuc = sonuc * carpan
print("4. Adım -> Çarpan:", carpan, "| Güncel Sonuç:", sonuc)
carpan = carpan + 1  # Sıradaki sayıya geç (5 oldu, işlem bitti!)

print("Döngüsüz 4! Sonucu:", sonuc)
print("-" * 55)

# ==============================================================================
# PEKİ YA 100! HESAPLAMAK İSTESEYDİK?
# Yukarıdaki aynı 3 satırlık kodu 100 defa alt alta kopyala-yapıştır mı yapacaktık?
# Tabii ki hayır! İşte tam burada devreye "while" (-iken / olduğu sürece) döngüsü girer.
#
# Dikkat ederseniz yukarıda sürekli tekrar eden işlem şu:
#   sonuc = sonuc * carpan
#   carpan = carpan + 1
#
# Bu işlemi "carpan sayısı, hedeflediğimiz sayıdan küçük veya eşit olduğu sürece"
# tekrarla dersek, bilgisayar bunu bizim yerimize otomatik yapar!
# ==============================================================================

print("\n--- 2. BÖLÜM: WHILE DÖNGÜSÜ İLE FAKTÖRİYEL ---")

hedef_sayi = 5  # Şimdi 5! (1*2*3*4*5 = 120) hesaplayalım
sonuc = 1       # Sonucu tutacak değişkenimiz
carpan = 1      # 1'den başlayıp hedef_sayi'ya kadar gidecek sayacımız

# KURAL: "carpan" değişkeni "hedef_sayi" değerine küçük veya eşit olduğu sürece döngü çalışsın:
while carpan <= hedef_sayi:
    sonuc = sonuc * carpan  # Mevcut sonucu sıradaki çarpan ile çarp
    print("Çarpan:", carpan, "iken -> Ara Sonuç:", sonuc)
    carpan = carpan + 1     # Çarpanı 1 artır ki bir sonraki sayıya geçebilelim (Unutursak sonsuz döngü olur!)

print(hedef_sayi, "sayısının faktöriyeli (", hedef_sayi, "! ) =", sonuc)


# sizden istenen ekleme kullanıcının girdiği sayının faktöryelini hesapyan kodu while döngüsü yazınız
