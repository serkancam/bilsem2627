ys=int(input("yıldız adedi:"))

"""
yıldız adedi:3
*
**
***
yıldız adedi:4
*
**
***
****
"""

for i in range(1,ys+1):
    print("*"*i)



for t in range(1,ys+1):
    for a in range(t):
        print("*",end="")
    print()

# for a in range(2):
#     print("*",end="")
# print()
"""
yıldız adedi:3
*
**
***
***
**
*
yıldız adedi:4
*
**
***
****
****
***
**
*
"""
for t in range(ys,0,-1):
    for a in range(t):
        print("*",end="")
    print()



