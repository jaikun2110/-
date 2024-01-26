# -*- coding: utf-8 -*-

# for

# for 변수 in 리스트
# for 변수 in 튜플
# for 변수 in 문자열

lst = [1,3,5,7,9]
for l in lst:
    print(l)
    
#%%    

t = 0
for l in lst:
    t += l

print("총합:", t)    

#%%

for char in "ABCDEFG":
    print(char)
