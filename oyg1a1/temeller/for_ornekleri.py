isim="serkan"
for harf in isim:
    # print(harf)
    if harf in "aeuıüoiö":
        print(harf.capitalize(),end="")
    else:
        print(harf,end="") 
print()



#3,6,9,12,15
for a in range(3,16,3):
    print(f"a:{a}")

#-3,1,5,9
for b in range(-3,10,3):
    print(f"b:{b}")
               
        
#21,14,7,0
for c in range(21,-1,-7):
    print(f"c:{c}")
               