# ==============================================================================
# KONU: PYTHON'DA FOR DÖNGÜSÜ, 'IN' VE 'RANGE()' KULLANIMI
# ==============================================================================
#
# 1. FOR DÖNGÜSÜ VE 'IN' OPERATÖRÜNÜN TEMEL MANTIĞI:
# - While döngüsü bir "koşul doğru olduğu sürece" çalışırken, 'for' döngüsü
#   belirli bir veri topluluğunun (dizi, liste, metin, sayı aralığı) elemanları
#   üzerinde TEKER TEKER gezmek (iterate etmek) için kullanılır.
# - 'in' anahtar kelimesi, bir koleksiyonun içindeki elemanları sırayla döngü
#   değişkenine atama görevini üstlenir ("liste İÇİNDEKİ her eleman için").
#
# 2. RANGE() FONKSİYONU NEDİR VE NASIL KULLANILIR?
# - range() fonksiyonu, belirli bir aralıkta sıralı tam sayılar üreten bir yapıdır.
# - Üç farklı şekilde kullanılabilir:
#
#   1) range(bitis):
#      0'dan başlar, bitiş değerine KADAR (bitiş dahil DEĞİLDİR) birer birer gider.
#      Örnek: range(5) -> 0, 1, 2, 3, 4 üretir.
#
#   2) range(baslangic, bitis):
#      Belirtilen başlangıçtan başlar, bitişe KADAR (bitiş dahil değil) gider.
#      Örnek: range(2, 7) -> 2, 3, 4, 5, 6 üretir.
#
#   3) range(baslangic, bitis, adim):
#      Başlangıçtan bitişe kadar belirtilen adım miktarı kadar artarak (veya azalarak) gider.
#      Örnek: range(1, 10, 2) -> 1, 3, 5, 7, 9 (Tek sayılar)
#      Örnek: range(5, 0, -1) -> 5, 4, 3, 2, 1 (Geriye doğru sayma)
# ==============================================================================

print("=" * 65)
print("1. BÖLÜM: DÖNGÜSÜZ (ELLE) TEKRAR VE FOR DÖNGÜSÜNE İHTİYAÇ")
print("=" * 65)

# Döngü bilmeseydik, 1'den 5'e kadar yazdırmak için 5 satır print yazardık:
print("Döngüsüz:")
print("Sayı: 1")
print("Sayı: 2")
print("Sayı: 3")
print("Sayı: 4")
print("Sayı: 5")

# Şimdi aynı işlemi 'for' ve 'range()' ile sadece 2 satırda yapalım:
print("\nFor Döngüsü ile:")
for sayi in range(1, 6):
    print("Sayı:", sayi)

print("-" * 65)


# ==============================================================================
# 2. BÖLÜM: RANGE() FONKSİYONUNUN 3 FARKLI KULLANIMI
# ==============================================================================
print("\n" + "=" * 65)
print("2. BÖLÜM: RANGE() FONKSİYONUNUN 3 FARKLI PARAMETRE KULLANIMI")
print("=" * 65)

# A) Tek Parametre: range(bitis) -> 0'dan 4'e kadar
print("A) range(5) Kullanımı (0'dan başlar, 5 DAHİL DEĞİL):")
for i in range(5):
    print(i, end=" ")
print()

# B) İki Parametre: range(baslangic, bitis)
print("\nB) range(3, 8) Kullanımı (3'ten başlar, 8 DAHİL DEĞİL):")
for i in range(3, 8):
    print(i, end=" ")
print()

# C) Üç Parametre: range(baslangic, bitis, adim)
print("\nC) range(2, 15, 3) Kullanımı (2'den başlar, 3'er 3'er artar):")
for i in range(2, 15, 3):
    print(i, end=" ")
print()

# D) Geriye Doğru Sayma: Negatif Adım
print("\nD) range(10, 0, -2) Kullanımı (10'dan başlar, 2'şer 2'şer azalır):")
for i in range(10, 0, -2):
    print(i, end=" ")
print()
print("-" * 65)


# ==============================================================================
# 3. BÖLÜM: 'IN' OPERATÖRÜ İLE STRİNG (METİN) VE LİSTE ÜZERİNDE GEZİNME
# ==============================================================================
# for döngüsü sadece sayılarda değil, bir metnin harfleri veya bir listenin
# elemanları üzerinde indeks kullanmaya gerek kalmadan doğrudan gezinir.
# ==============================================================================
print("\n" + "=" * 65)
print("3. BÖLÜM: METİNLER (STRING) VE LİSTELER ÜZERİNDE FOR DÖNGÜSÜ")
print("=" * 65)

# String üzerinde doğrudan gezinme:
mesaj = "BİLSEM"
print("'" + mesaj + "' kelimesinin harfleri:")
for harf in mesaj:
    print("Harf ->", harf)

print("-" * 40)

# Liste üzerinde gezinme:
notlar = [85, 90, 78, 95, 100]
toplam = 0

print("Öğrenci Notları:", notlar)
for n in notlar:
    toplam = toplam + n
    print("İncelenen not:", n, "| Ara Toplam:", toplam)

ortalama = toplam / len(notlar)
print("Sınıf Not Ortalaması:", ortalama)
print("-" * 65)


# ==============================================================================
# 4. BÖLÜM: ENUMERATE() İLE HEM İNDEKSİ HEM ELEMANI AYNI ANDA ALMA
# ==============================================================================
# Bazen döngüde hem sıraya (indekse) hem de elemanın kendisine ihtiyaç duyarız.
# Bunun için 'enumerate()' fonksiyonu kullanılır.
# ==============================================================================
print("\n" + "=" * 65)
print("4. BÖLÜM: ENUMERATE() İLE İNDEKS VE ELEMAN BİRLİKTE KULLANIMI")
print("=" * 65)

sehirler = ["Edirne", "İstanbul", "Ankara", "İzmir"]

# enumerate() her adımda bize (indeks, eleman) ikilisini verir:
for sira, sehir in enumerate(sehirler, start=1):
    print(f"{sira}. Şehir: {sehir}")

print("-" * 65)


# ==============================================================================
# 5. BÖLÜM: UYGULAMA ÖRNEĞİ (1'den N'e Kadar Olan Çift Sayıların Toplamı)
# ==============================================================================
print("\n" + "=" * 65)
print("5. BÖLÜM: ÖRNEK ALGORİTMA (1 - 20 ARASINDAKİ ÇİFT SAYILARIN TOPLAMI)")
print("=" * 65)

cift_toplam = 0

# range(2, 21, 2) ile doğrudan çift sayıları üretiyoruz
for cift_sayi in range(2, 21, 2):
    cift_toplam = cift_toplam + cift_sayi
    print(f"Eklenen çift sayı: {cift_sayi:2d} | Güncel Toplam: {cift_toplam}")

print(f"\nSonuç: 1 ile 20 arasındaki çift sayıların toplamı = {cift_toplam}")
print("=" * 65)
