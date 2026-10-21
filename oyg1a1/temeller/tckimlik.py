tc_9=input("tc ilk 9 rakamı girin:")

b0=int(tc_9[0])
b1=int(tc_9[1])
b2=int(tc_9[2])
b3=int(tc_9[3])
b4=int(tc_9[4])
b5=int(tc_9[5])
b6=int(tc_9[6])
b7=int(tc_9[7])
b8=int(tc_9[8])

b9=(7*(b0+b2+b4+b6+b8)-(b1+b3+b5+b7))%10
b10=(b0+b1+b2+b3+b4+b5+b6+b7+b8+b9)%10
print(b9,b10)