# ==============================================================================
# KONU 3: ÖKLİD ALGORİTMASI İLE EBOB (En Büyük Ortak Bölen)
# ==============================================================================
#
# 1. TANIM VE KÂĞIT-KALEM İLE ELLE ÇÖZÜM:
# İki sayıyı aynı anda kalansız bölebilen en büyük sayıya EBOB denir.
# Büyük sayılarda tek tek bölen denemek çok uzun sürer. Bunun yerine M.Ö. 300 yılında
# matematikçi Öklid'in bulduğu harika bir yöntem (Öklid Algoritması) kullanılır.
#
# ÖKLİD KURALI ŞÖYLEDİR:
# 1. Büyük sayıyı küçük sayıya böl ve KALANI bul (Python'da kalan bulma operatörü: %).
# 2. Artık büyük sayıyla işimiz bitti!
#    - Eski "küçük sayı" -> yeni "büyük sayı" olur.
#    - Bulduğumuz "kalan" -> yeni "küçük sayı" olur.
# 3. Küçük sayı (yani kalan) 0 olana kadar bu bölme ve kaydırma işlemine devam et!
# 4. Küçük sayı 0 olduğunda, elimizdeki büyük sayı bize EBOB'u verir!
#
# Kağıt üzerinde 48 ve 18 sayılarının EBOB'unu bulalım:
# Başlangıç: buyuk = 48, kucuk = 18
#
# 1. Adım: 48'i 18'e böl -> Kalan = 12 (Çünkü 18 * 2 = 36, 48 - 36 = 12).
#          Kaydır: buyuk = 18 oldu, kucuk = 12 oldu.
#
# 2. Adım: 18'i 12'ye böl -> Kalan = 6  (Çünkü 12 * 1 = 12, 18 - 12 = 6).
#          Kaydır: buyuk = 12 oldu, kucuk = 6 oldu.
#
# 3. Adım: 12'yi 6'ya böl -> Kalan = 0  (Çünkü 6 * 2 = 12, 12 - 12 = 0).
#          Kaydır: buyuk = 6 oldu, kucuk = 0 oldu.
#
# DUR! Küçük sayı 0 oldu! O halde EBOB = 6'dır.
# ==============================================================================

print("--- 1. BÖLÜM: DÖNGÜSÜZ (ELLE ADIM ADIM) ÖKLİD ALGORİTMASI ---")

buyuk = 48
kucuk = 18
print("Başlangıç -> Büyük Sayı:", buyuk, "| Küçük Sayı:", kucuk)

# 1. Adım:
kalan = buyuk % kucuk  # % işareti bölme işleminden kalanı verir (48 % 18 = 12)
buyuk = kucuk          # Küçük sayı, büyük sayının yerine geçti (18)
kucuk = kalan          # Kalan ise küçük sayının yerine geçti (12)
print("1. Adım Sonucu -> Büyük:", buyuk, "| Küçük (Kalan):", kucuk)

# 2. Adım:
kalan = buyuk % kucuk  # 18 % 12 = 6
buyuk = kucuk          # buyuk = 12 oldu
kucuk = kalan          # kucuk = 6 oldu
print("2. Adım Sonucu -> Büyük:", buyuk, "| Küçük (Kalan):", kucuk)

# 3. Adım:
kalan = buyuk % kucuk  # 12 % 6 = 0
buyuk = kucuk          # buyuk = 6 oldu
kucuk = kalan          # kucuk = 0 oldu
print("3. Adım Sonucu -> Büyük:", buyuk, "| Küçük (Kalan):", kucuk)

# Küçük sayı 0 olduğu için işlem bitti!
print("Döngüsüz Hesaplanan EBOB:", buyuk)
print("-" * 55)

# ==============================================================================
# SIRA SENDE! (ÖĞRENCİ GÖREVİ - WHILE DÖNGÜSÜ İLE ÇÖZÜM)
# ==============================================================================
# Yukarıdaki 1., 2. ve 3. adımlara dikkatlice bak!
# Her adımda şu 3 satır kendini tekrar ediyor:
#
#   kalan = buyuk % kucuk
#   buyuk = kucuk
#   kucuk = kalan
#
# Peki biz bu işlemi ne zamana kadar tekrarlıyoruz?
# -> "kucuk" değişkeni 0'dan farklı olduğu sürece (veya kucuk > 0 olduğu sürece)!
#
# GÖREVİN:
# Aşağıda verilen 105 ve 42 sayılarının EBOB'unu, adımları tek tek elle yazmadan,
# sadece bir "while" döngüsü kullanarak hesaplayan kodu tamamla!
#
# İPUCU SORULARI:
# 1. while döngüsünün koşulu ne olmalı? (Hangi değişken 0'dan büyük olduğu sürece döngü dönmeli?)
# 2. Döngünün içine hangi 3 satırlık tekrar eden kodu yazmalısın?
# 3. Döngü bittiğinde sonucu hangi değişkenin içinde ekrana yazdırmalısın?
# ==============================================================================

print("\n--- 2. BÖLÜM: SIRA SENDE! (WHILE DÖNGÜSÜNÜ SEN YAZ) ---")

buyuk = 105
kucuk = 42

# TODO: Aşağıdaki yorum satırlarını silip kendi while döngünü buraya yaz!

# while .................... :
#     kalan = ................
#     buyuk = ................
#     kucuk = ................

# print("105 ve 42 sayılarının EBOB değeri:", buyuk)
