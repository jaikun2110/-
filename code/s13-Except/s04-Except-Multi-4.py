# -*- coding: utf-8 -*-

# 예외처리
# 여러 예외를 처리

x = 10
y = 0
z = None

# 아래 변수(c)를 주석으로 막으면 NameError 예외발생
# c = 0

try:
    print("x=", x)
    print("y=", y)
    print("c=", c)
    z = x / y
except (ZeroDivisionError, NameError) as e:
    print("[예외발생] ", e)    
    
    
print(f"결과:{x} / {y} -> {z}")    