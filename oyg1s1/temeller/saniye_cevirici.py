"""
saniye olarak girilen değeri gün:saat:dakika:saniye şeklinde veren kodu yazınız
"""
sure_saniye=int(input("saniye cinsinden süreyi giriniz:"))

"""
1362--> 0 gün:0 saat:22 dakika:42 saniye
951650-->saniye 50:dakika20:saat 0:gün 11

"""
saniye=sure_saniye%60
dakika=((sure_saniye-saniye)//60)%60
saat=(((sure_saniye-saniye)//60)//60)%24
gun=(((sure_saniye-saniye)//60)//60)//24
print(f"{gun}:{saat}:{dakika}:{saniye}")
"""
saniye=sure_saniye%60
dakika=((sure_saniye-saniye)//60)%60
saat=(sure_saniye-dakika*60-saniye)//60%60
gun=(sure_saniye-saat*60*60-dakika*60-saniye)//(3600)//24
"""

