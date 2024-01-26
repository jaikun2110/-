# 16진수(Hexa-Decimal)
# 0x or 0X : 0xff, 0XFF

# 10진수: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 16진수: 1 2 3 4 5 6 7 8 9  a  b  c  d  e  f
# 16진수: 1 2 3 4 5 6 7 8 9  A  B  C  D  E  F

#  2진수 : 1111 1111
# 16진수 :    F    F : 0xff, 0XFF
# 10진수 : 255
#  2진수 : 11 111 111
#  8진수 :  3   7   7 : 0o377

#%%

d = 255
h = 0xff
o = 0o377
H = 0XFF
O = 0O377

print(d == h)  # True
print(d == o)  # True
print(h == o)  # True
print(d, h, o) # 255 255 255
print(H, O) # 255 255
