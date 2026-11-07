metin=input("metin gir:")
harf=input("aranacak harf:")

"""
kullanıcının girdiği metinde aranacak harften kaç adet olduğunu bulan kodu python ile yazınız.
"""

adet=0

###çözümü buraya yazınız

for hr in metin:
    # print(hr)
    if hr.lower()==harf.lower():
        adet=adet+1



print(f"metinde {adet} {harf} harfi var:")