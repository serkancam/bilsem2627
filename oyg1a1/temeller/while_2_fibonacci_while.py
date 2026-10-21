# ==============================================================================
# KONU 2: FİBONACCİ DİZİSİ (Adım Adım While Döngüsüne Geçiş)
# ==============================================================================
#
# 1. TANIM VE KÂĞIT-KALEM İLE ELLE ÇÖZÜM:
# Fibonacci dizisi, 0 ve 1 ile başlayan ve her yeni sayının kendisinden önceki
# İKİ sayının toplamı olduğu özel bir sayı dizisidir.
#
# Dizinin ilk terimleri: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
#
# Kağıt üzerinde adım adım nasıl buluyoruz?
# Başlangıç: İlk sayı (a) = 0, İkinci sayı (b) = 1
#
# 1. Adım: Yeni sayı = 0 + 1 = 1  (Artık son iki sayımız 1 ve 1 oldu)
# 2. Adım: Yeni sayı = 1 + 1 = 2  (Artık son iki sayımız 1 ve 2 oldu)
# 3. Adım: Yeni sayı = 1 + 2 = 3  (Artık son iki sayımız 2 ve 3 oldu)
# 4. Adım: Yeni sayı = 2 + 3 = 5  (Artık son iki sayımız 3 ve 5 oldu)
# 5. Adım: Yeni sayı = 3 + 5 = 8  (Artık son iki sayımız 5 ve 8 oldu)
#
# KAYDIRMA KURALI: Her adımda yeni sayıyı bulduktan sonra;
# - Eski "ikinci sayı" artık yeni "birinci sayı" olur.
# - Bulduğumuz "yeni toplam" ise artık yeni "ikinci sayı" olur.
# ==============================================================================

print("--- 1. BÖLÜM: DÖNGÜSÜZ (ELLE ADIM ADIM) FİBONACCİ ---")

# İlk 6 Fibonacci sayısını döngü KULLANMADAN ekrana yazdıralım:
birinci = 0
ikinci = 1

print("1. Terim:", birinci)
print("2. Terim:", ikinci)

# 3. Terimi Bulalım:
yeni = birinci + ikinci
print("3. Terim:", yeni)
birinci = ikinci  # Kaydırma yapıyoruz: ikinci sayı, birinci koltuğuna geçti (1)
ikinci = yeni     # Yeni bulduğumuz sayı, ikinci koltuğuna geçti (1)

# 4. Terimi Bulalım:
yeni = birinci + ikinci
print("4. Terim:", yeni)
birinci = ikinci  # Kaydırma: birinci = 1 oldu
ikinci = yeni     # Kaydırma: ikinci = 2 oldu

# 5. Terimi Bulalım:
yeni = birinci + ikinci
print("5. Terim:", yeni)
birinci = ikinci  # Kaydırma: birinci = 2 oldu
ikinci = yeni     # Kaydırma: ikinci = 3 oldu

# 6. Terimi Bulalım:
yeni = birinci + ikinci
print("6. Terim:", yeni)
birinci = ikinci  # Kaydırma: birinci = 3 oldu
ikinci = yeni     # Kaydırma: ikinci = 5 oldu

print("-" * 55)

# ==============================================================================
# DÖNGÜYE GEÇİŞ MANTIĞI:
# Yukarıdaki kodda 3. terimden itibaren şu 4 satırın birebir aynı olduğunu fark ettiniz mi?
#
#   yeni = birinci + ikinci
#   print(yeni)
#   birinci = ikinci
#   ikinci = yeni
#
# Eğer bizden 50 tane Fibonacci sayısı istenseydi, bu 4 satırı 50 kere alt alta yazmak
# yerine bir "sayac" tutarız ve "sayac <= 50 olduğu sürece (while)" bu 4 satırı çalıştırırız!
# ==============================================================================

print("\n--- 2. BÖLÜM: WHILE DÖNGÜSÜ İLE FİBONACCİ ---")

toplam_terim_sayisi = 8  # İlk 8 Fibonacci sayısını bulalım
birinci = 0
ikinci = 1
sayac = 1  # Kaçıncı terimde olduğumuzu takip eden değişken

# Sayacımız, istediğimiz terim sayısına küçük veya eşit olduğu sürece devam et:
while sayac <= toplam_terim_sayisi:
    print(sayac, ". Terim ->", birinci)
    
    # Sıradaki toplamı hesapla ve sayıları birer basamak kaydır
    yeni = birinci + ikinci
    birinci = ikinci
    ikinci = yeni
    
    # Bir terim yazdırdığımız için sayacı 1 artırıyoruz
    sayac = sayac + 1
