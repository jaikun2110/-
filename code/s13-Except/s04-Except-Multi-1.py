# -*- coding: utf-8 -*-

# 예외처리
# 여러 예외를 처리

x = 10
y = 0
z = None

# 아래 변수(c)를 주석으로 막으면 NameError 예외발생
c = 0

try:
    print("x=", x)
    print("y=", y)
    print("c=", c)
    z = x / y
except ZeroDivisionError as e:
    print("[예외발생] 0으로 나눌 수 없습니다.", e)    
except NameError as e:
    print("[예외발생] 선언되지 않은 변수가 있습니다.",e)    
    
    
print(f"결과:{x} / {y} -> {z}")    