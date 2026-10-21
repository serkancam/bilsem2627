# ingiliz harfleri, rakamlar, alt çizgi.
# rakam başa gelşemez.
# su ve tuz birim miktarı verilen bir karışımdaki tuz oranını bulan program

tuz_miktari=int(input("tuz miktarini gir:"))
su_miktari=int(input("su miktari gir:"))

karisim_miktari=tuz_miktari+su_miktari

tuz_orani=(tuz_miktari*100)/karisim_miktari

print(tuz_orani)