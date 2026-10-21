# derisim_hesap.py
"""
su ve tuz miktarı girilen bir programın karışımdaki tuz oranı yüzdesini veren kodu yazınız.
"""
tuz_miktar=int(input("tuz miktarı:"))
su_miktarı=int(input("su miktarı:"))

toplam_miktar=tuz_miktar+su_miktarı

tuz_orani=(tuz_miktar*100)/toplam_miktar

print(f"tuz oranı:{tuz_orani}")

