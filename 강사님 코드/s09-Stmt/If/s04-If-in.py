# -*- coding: utf-8 -*-
# If문
# x in s : s안에 x값이 존재하는지 유무
# x not in s : s안에 x값이 존재하지 않는지 유무

s = [1,3,5,7,9]
x = 2

if x in s:
    print(f"{s} 안에 값({x})이 존재함")
else:
    print(f"{s} 안에 값({x})이 존재하지 않음")
    
#%%    

exist = x in s

if exist: # 변수(exist)의 값이 True이면?
    print(f"{s} 안에 값({x})이 존재함")
else:
    print(f"{s} 안에 값({x})이 존재하지 않음")
    
#%%

# not in
# s에 10이 존재하지 않으면 참(True)
x = 10
exist = x not in s

if exist: # 변수(exist)의 값이 True이면?
    print(f"{s} 안에 값({x})이 존재하지 않음")
else:
    print(f"{s} 안에 값({x})이 존재함")
    
#%%

x = 10
exist = x in s

if exist != True: 
    print(f"{s} 안에 값({x})이 존재하지 않음")
else:
    print(f"{s} 안에 값({x})이 존재함")
    