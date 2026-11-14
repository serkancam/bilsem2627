Soru 1: Algoritmada dikkat edilmesi gereken kurallardan 4 tanesini yazınız.

1. **Başlangıç ve Bitiş:** Algoritmanın mutlaka net bir başlangıç ve bitiş noktası olmalıdır.
2. **Kesinlik (Belirlilik):** Her adım açık, net ve tek bir anlama gelecek şekilde ifade edilmelidir; yoruma açık olmamalıdır.
3. **Sonluluk:** Algoritma sonsuz döngüye girmeden belirli ve sınırlı sayıda adımda tamamlanmalıdır.
4. **Etkinlik (Uygulanabilirlik):** Her adım temel, mantıklı ve bilgisayar veya insan tarafından uygulanabilir olmalıdır.

---

Soru 2: Python programlama dilinin diğer dillere kıyasla tercih edilme nedenlerinden (neden Python?) 2 tanesini belirtiniz.

1. **Sözdiziminin (Syntax) Basitliği ve Okunabilirlik:** İngilizceye yakın, sade ve temiz bir yazıma sahiptir; öğrenmesi ve geliştirmesi hızlıdır.
2. **Geniş Kütüphane Desteği:** Yapay zekâ, veri analizi, web geliştirme ve otomasyon gibi alanlarda hazır zengin modül/kütüphane ekosistemine sahiptir.

---

Soru 3: Bilgisayara girilen bir yıl değerine göre o yıldaki Şubat ayının 28 veya 29 gün olduğunu bulan programın algoritma ve akış şemasını hazırlayınız.

*Algoritma:*

* Adım 1: Başla.
* Adım 2: Kullanıcıdan `yil` değerini al.
* Adım 3: Eğer (`yil % 4 == 0` ve `yil % 100 != 0`) veya (`yil % 400 == 0`) ise;
* Ekrana "Şubat 29 gündür (Artık yıl)" yaz.
* Değilse; Ekrana "Şubat 28 gündür" yaz.


* Adım 4: Bitir.

*Akış Şeması Sembolleri/Akışı:*

* `[Elips]` Başla
* `[/Paralelkenar/]` Giriş: `yil`
* `<Eşkenar Dörtgen>` Karar: `(yil % 4 == 0 ve yil % 100 != 0) veya (yil % 400 == 0)`
* *Evet:* `[/Dalgalı Dörtgen/]` Çıktı: "Şubat 29 gündür"
* *Hayır:* `[/Dalgalı Dörtgen/]` Çıktı: "Şubat 28 gündür"


* `[Elips]` Bitir

---

Soru 4: Su tüketim miktarına göre fatura tutarını hesaplayan programın algoritma ve akış şemasını hazırlayınız. (15 tonun altında 5 TL/ton, 15 ton ve üzerinde 7 TL/ton)

*Algoritma:*

* Adım 1: Başla.
* Adım 2: Tüketilen su miktarını (`miktar`) kullanıcıdan al.
* Adım 3: Eğer `miktar < 15` ise:
* `tutar = miktar * 5`
* Değilse:
* `tutar = miktar * 7`


* Adım 4: Ekrana `tutar` değerini yazdır.
* Adım 5: Bitir.

*Akış Şeması Sembolleri/Akışı:*

* `[Elips]` Başla
* `[/Paralelkenar/]` Giriş: `miktar`
* `<Eşkenar Dörtgen>` Karar: `miktar < 15`
* *Evet:* `[Dikdörtgen]` İşlem: `tutar = miktar * 5`
* *Hayır:* `[Dikdörtgen]` İşlem: `tutar = miktar * 7`


* `[/Dalgalı Dörtgen/]` Çıktı: `tutar`
* `[Elips]` Bitir

---

Soru 5: Arabayı çalıştırıp ve araç sürme algoritmasını yazınız.

* Adım 1: Başla.
* Adım 2: Aracın kapısını açıp sürücü koltuğuna otur ve kapıyı kapat.
* Adım 3: Emniyet kemerini tak, dikiz ve yan aynaları ayarla.
* Adım 4: Debriyaja ve frene bas (otomatik viteste sadece frene bas).
* Adım 5: Kontak anahtarını çevirerek (veya Start tuşuna basarak) motoru çalıştır.
* Adım 6: El frenini indir.
* Adım 7: Vitesi 1'e (otomatik ise D konumuna) al.
* Adım 8: Kalkış yönüne uygun sinyali ver.
* Adım 9: Freni bırakıp hafifçe gaza basarak aracı hareket ettir ve sürüşe başla.
* Adım 10: Bitir.

---

Soru 6: Ekrana 10 defa programcının adını yazan programın algoritma ve akış şemasını hazırlayınız.

*Algoritma:*

* Adım 1: Başla.
* Adım 2: `sayac = 1` değerini ata.
* Adım 3: Ekrana "Programcı Adı" yaz.
* Adım 4: `sayac = sayac + 1` işlemini yap.
* Adım 5: Eğer `sayac <= 10` ise Adım 3'e dön.
* Adım 6: Bitir.

*Akış Şeması Sembolleri/Akışı:*

* `[Elips]` Başla
* `[Dikdörtgen]` İşlem: `sayac = 1`
* `[/Dalgalı Dörtgen/]` Çıktı: "Programcı Adı"
* `[Dikdörtgen]` İşlem: `sayac = sayac + 1`
* `<Eşkenar Dörtgen>` Karar: `sayac <= 10`
* *Evet:* Çıktı adımına geri dön.
* *Hayır:* Devam et.


* `[Elips]` Bitir

---

Soru 7: 1'den 100'e kadar tek sayıları yazdıran programın algoritma ve akış şemasını hazırlayınız.

*Algoritma:*

* Adım 1: Başla.
* Adım 2: `sayi = 1` ata.
* Adım 3: Ekrana `sayi` değerini yaz.
* Adım 4: `sayi = sayi + 2` işlemini yap.
* Adım 5: Eğer `sayi < 100` ise Adım 3'e dön.
* Adım 6: Bitir.

*Akış Şeması Sembolleri/Akışı:*

* `[Elips]` Başla
* `[Dikdörtgen]` İşlem: `sayi = 1`
* `[/Dalgalı Dörtgen/]` Çıktı: `sayi`
* `[Dikdörtgen]` İşlem: `sayi = sayi + 2`
* `<Eşkenar Dörtgen>` Karar: `sayi < 100`
* *Evet:* Çıktı adımına geri dön.
* *Hayır:* Devam et.


* `[Elips]` Bitir

---

Soru 8: Python'da kullanıcıdan klavye aracılığıyla veri almak için hangi fonksiyon kullanılır?

* `input()` fonksiyonu kullanılır.

---

Soru 9: Aşağıdaki koda göre ekrana hangi çıktı verilir?

Kod adımları takibi:

* `puan = 50` -> `print("İlk puan:", puan)` -> **`İlk puan: 50`**


* `puan = 70` -> `print("Sınav sonrası puan:", puan)` -> **`Sınav sonrası puan: 70`**


* `puan = puan + 10` (80) -> `print("Ek puan sonrası:", puan)` -> **`Ek puan sonrası: 80`**


* `puan += 5` (85) -> `print("Son puan:", puan)` -> **`Son puan: 85`**


* `print("Program sonunda öğrencinin puanı:", puan)` -> **`Program sonunda öğrencinin puanı: 85`**



*Konsol Çıktısı:*

```text
İlk puan: 50
Sınav sonrası puan: 70
Ek puan sonrası: 80
Son puan: 85
Program sonunda öğrencinin puanı: 85

```

---

Soru 10: Üniversite öğrencisinin dönem geçme notunu hesaplayıp geçme/kalma durumunu ekranda gösteren programın algoritması ve akış şeması.
(İki vize, bir final. Vize ortalamasının %40'ı + finalin %60'ı. Geçme notu: 50)

*Algoritma:*

* Adım 1: Başla.
* Adım 2: `vize1`, `vize2` ve `final` notlarını kullanıcıdan al.
* Adım 3: `vize_ort = (vize1 + vize2) / 2` hesapla.
* Adım 4: `ortalama = (vize_ort * 0.40) + (final * 0.60)` hesapla.
* Adım 5: Eğer `ortalama >= 50` ise:
* Ekrana "Geçti, Notunuz: ", `ortalama` yazdır.
* Değilse:
* Ekrana "Kaldı, Notunuz: ", `ortalama` yazdır.


* Adım 6: Bitir.

*Akış Şeması Sembolleri/Akışı:*

* `[Elips]` Başla
* `[/Paralelkenar/]` Giriş: `vize1, vize2, final`
* `[Dikdörtgen]` İşlem: `vize_ort = (vize1 + vize2) / 2`
* `[Dikdörtgen]` İşlem: `ortalama = (vize_ort * 0.4) + (final * 0.6)`
* `<Eşkenar Dörtgen>` Karar: `ortalama >= 50`
* *Evet:* `[/Dalgalı Dörtgen/]` Çıktı: "Geçti"
* *Hayır:* `[/Dalgalı Dörtgen/]` Çıktı: "Kaldı"


* `[Elips]` Bitir

---

Soru 11: Python editörlerinden 2 tane yazınız.

1. **Visual Studio Code (VS Code)**
2. **PyCharm** *(veya IDLE, Thonny, Spyder)*

---

Soru 12: Kodda `notu = 75` olan bir öğrenci için ekrana hangi çıktı verilir?

* İnceleme:
* `if notu >= 85:` -> 75 >= 85 yanlış (False)


* `elif notu >= 70:` -> 75 >= 70 doğru (True) -> `print("İyi")` çalışır ve bloktan çıkılır.




* **Ekran Çıktısı:**

```text
İyi

```

---

Soru 13: Derleyici ve yorumlayıcı arasındaki farklardan 1 tane yazınız.

* **Çeviri ve Çalışma Şekli:** Derleyici (Compiler) kaynak kodun tamamını tek seferde makine diline çevirerek bağımsız çalışabilir bir hedef dosya (.exe vb.) üretir; yorumlayıcı (Interpreter) ise kodu satır satır okur, anlık olarak yorumlayıp doğrudan çalıştırır.