# -*- coding: utf-8 -*-

# 예외처리
# 여러 예외를 처리

l = [0,1,3,5,7,9]

print(l[0], l[5]) # 0 9
print(l[6]) # IndexError: list index out of range

#%%
x = 10
y = 1
z = None

# 아래 변수(c)를 주석으로 막으면 NameError 예외발생
c = 0

try:
    print("x=", x)
    print("y=", y)
    print("c=", c)
    z = x // y
    print(f"z({z}), {l[z]}") # z(10), l[10]
except (ZeroDivisionError, NameError, IndexError) as e:
    print("[예외발생] ", e)    
    
    
print(f"결과:{x} / {y} -> {z}")    