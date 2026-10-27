# ==============================================================================
# KONU: PYTHON'DA WHILE DÖNGÜSÜ İLE STRİNG (METİN) KULLANIMI
# SENARYO: KULLANICI ŞİFRESİ VE METİN ANALİZİ (GÜVENLİK VE KARAKTER DENETİMİ)
# ==============================================================================
#
# 1. STRİNG'LERİN (METİNLERİN) TEMEL MANTIĞI:
# Python'da bir string, karakterlerin yan yana dizildiği bir koleksiyondur.
# Tıpkı bir listenin elemanları gibi, string içerisindeki her karaktere 0'dan 
# başlayan bir "indeks (sıra numarası)" ile erişilebilir.
#
# Örnek: kelime = "BİLGİ"
#   İndeks:  0 -> 'B'
#            1 -> 'İ'
#            2 -> 'L'
#            3 -> 'G'
#            4 -> 'İ'
#   Karakter Sayısı (Uzunluk): len(kelime) = 5
#   Son İndeks: len(kelime) - 1 = 4
#
# ==============================================================================
# 2. BU ÖRNEKTE KULLANILAN STRİNG FONKSİYONLARI VE ÖZELLİKLERİ:
# ==============================================================================
# 1) len(metin):
#    - Metnin toplam kaç karakterden oluştuğunu (uzunluğunu) tam sayı olarak döndürür.
#    - While döngüsünün durma koşulunu belirlerken (indeks < len(metin)) kullanılır.
#
# 2) metin.strip():
#    - Metnin başındaki ve sonundaki gereksiz boşlukları (veya enter karakterlerini) temizler.
#    - Örneğin: "  gizli  ".strip() -> "gizli" olur.
#
# 3) karakter.isupper():
#    - İlgili karakter BÜYÜK harf ise True, değilse False döndürür.
#
# 4) karakter.islower():
#    - İlgili karakter KÜÇÜK harf ise True, değilse False döndürür.
#
# 5) karakter.isdigit():
#    - İlgili karakter bir RAKAM ('0'-'9') ise True, değilse False döndürür.
#
# 6) metin.lower():
#    - Metindeki tüm büyük harfleri küçük harfe dönüştürür.
#
# 7) metin.upper():
#    - Metindeki tüm küçük harfleri büyük harfe dönüştürür.
# ==============================================================================

print("=" * 60)
print("1. BÖLÜM: DÖNGÜSÜZ (ELLE ADIM ADIM) STRİNG GEZME")
print("=" * 60)

# "KOD" kelimesinin harflerini ve türlerini döngü KULLANMADAN inceleyelim:
kelime = "K1a"
print("İncelenen Kelime:", kelime)
print("Kelimenin Uzunluğu len(kelime):", len(kelime))
print("-" * 40)

indeks = 0  # 0. indexten başlıyoruz

# 0. Karakter (1. Adım)
karakter = kelime[indeks]
print("İndeks:", indeks, "| Karakter:", karakter, "| Büyük harf mi?:", karakter.isupper())
indeks = indeks + 1  # Bir sonraki harfe geç

# 1. Karakter (2. Adım)
karakter = kelime[indeks]
print("İndeks:", indeks, "| Karakter:", karakter, "| Rakam mı?:", karakter.isdigit())
indeks = indeks + 1  # Bir sonraki harfe geç

# 2. Karakter (3. Adım)
karakter = kelime[indeks]
print("İndeks:", indeks, "| Karakter:", karakter, "| Küçük harf mi?:", karakter.islower())
indeks = indeks + 1  # indeks 3 oldu (len(kelime) değerine ulaştı, bitti!)

print("Elle kontrol bitti. Dikkat ettiyseniz her adımda şu 2 işlem tekrar etti:")
print("  1) karakter = kelime[indeks]")
print("  2) indeks = indeks + 1")
print("-" * 60)


# ==============================================================================
# 2. BÖLÜM: WHILE DÖNGÜSÜ İLE GELİŞMİŞ ŞİFRE VE METİN ANALİZİ
# ==============================================================================
# Senaryo: Öğrencilerin girdiği bir parolanın güvenlik analizi:
# - Kaç adet büyük harf var?
# - Kaç adet küçük harf var?
# - Kaç adet rakam var?
# - Kaç adet özel karakter/sembol var?
# ==============================================================================

print("" + "=" * 60)
print("2. BÖLÜM: WHILE DÖNGÜSÜ İLE KARAKTER KARAKTER PAROLA ANALİZİ")
print("=" * 60)

# Analiz edilecek örnek parola (başında ve sonunda kasıtlı boşluk bırakıldı)
ham_parola = "  Python2026!#  "

# 1. Fonksiyon Kullanımı: strip() ile gereksiz boşlukları kırpalım
parola = ham_parola.strip()

print("Ham Parola              :", repr(ham_parola))
print("strip() Yapılmış Parola :", repr(parola))
print("Toplam Karakter Sayısı  :", len(parola))
print("-" * 40)

# Sayaçlarımızı ve kontrol değişkenlerimizi başlatalım
buyuk_sayisi = 0
kucuk_sayisi = 0
rakam_sayisi = 0
ozel_karakter_sayisi = 0

i = 0  # Döngü indisi (0'dan len(parola)-1'e kadar gidecek)

# WHILE KOŞULU:
# İndeks (i) metnin uzunluğundan (len) küçük olduğu sürece devam et:
while i < len(parola):
    harf = parola[i]  # i. indisteki karakteri al
    
    # Karakterin tipini string fonksiyonlarıyla denetle
    if harf.isupper():
        buyuk_sayisi = buyuk_sayisi + 1
        durum = "Büyük Harf"
    elif harf.islower():
        kucuk_sayisi = kucuk_sayisi + 1
        durum = "Küçük Harf"
    elif harf.isdigit():
        rakam_sayisi = rakam_sayisi + 1
        durum = "Rakam"
    else:
        ozel_karakter_sayisi = ozel_karakter_sayisi + 1
        durum = "Özel Karakter / Sembol"
    
    print(f"İndeks [{i}] -> '{harf}' : {durum}")
    
    # SAYACI ARTIR: Bunu unutursak 'i' hep 0 kalır ve SONSUZ DÖNGÜYE girer!
    i = i + 1

print("-" * 40)
print("ANALİZ RAPORU:")
print("  - Büyük Harf Adedi      :", buyuk_sayisi)
print("  - Küçük Harf Adedi      :", kucuk_sayisi)
print("  - Rakam Adedi           :", rakam_sayisi)
print("  - Özel Karakter Adedi   :", ozel_karakter_sayisi)
print("=" * 60)


# ==============================================================================
# 3. BÖLÜM: WHILE İLE STRİNG'İ TERSTEN YAZDIRMA (PALİNDROM MANTIĞI)
# ==============================================================================
# While döngüsü sadece ileriye değil, geriye doğru da sayabilir!
# İndeksi metnin sonundan (len(kelime) - 1) başlatıp 0'a kadar azaltırsak
# metni döngüyle ters çevirmiş oluruz.
# ==============================================================================

print("" + "=" * 60)
print("3. BÖLÜM: WHILE İLE METNİ TERSTEN OLUŞTURMA")
print("=" * 60)

orijinal_metin = "BİLSEM"
ters_metin = ""

# Sondaki karakterin indeksi her zaman (uzunluk - 1)'dir:
ters_indeks = len(orijinal_metin) - 1

print("Orijinal Metin:", orijinal_metin)

# İndeks 0 veya daha büyük olduğu sürece geriye doğru git:
while ters_indeks >= 0:
    secilen_harf = orijinal_metin[ters_indeks]
    ters_metin = ters_metin + secilen_harf  # Metin birleştirme (concatenation)
    print(f"Adım -> Eklenen Harf: '{secilen_harf}' | Güncel Ters Metin: {ters_metin}")
    
    ters_indeks = ters_indeks - 1  # Bir önceki karaktere geri git!

print("-" * 40)
print("Sonuç:")
print("Düz Hali :", orijinal_metin)
print("Ters Hali:", ters_metin)
print("=" * 60)
