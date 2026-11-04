import time
import os

os.system("clear")
dks=""
sns=""
for dk in range(0,11):
    for sn in range(0,60):
        sns=sn
        dks=dk
        if dk<10:
            dks="0"+str(dk)           
        if sn<10:
            sns="0"+str(sn)      
     
        print(f"{dks}:{sns}")

        time.sleep(1)
        os.system("clear")