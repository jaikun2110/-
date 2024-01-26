# bool
# is, not is

#%%

a = 10
b = 20
c = 10

b1 = a is b     # a == b
b2 = not a is b # a != b
b3 = a is c     # a == c
b4 = not a is c # a != c

print(b1)   # False
print(b2)   # True
print(b3)   # True
print(b4)   # False
