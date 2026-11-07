import os
import time

for dk in range(10):
    for sn in range(60): 
        os.system("clear")
        print(f"{dk}:{sn}")
        time.sleep(1)   


#bütün çıktılar 00:00 formatında olacak şekilde kodu güncelleyiniz.
"""
şu anda dakika veya saniye 10 değerinden her küçük olduğu durum için tek basamak yazdırılıyor.
örneğin 
0:7 --> 00:07 olsun.
"""