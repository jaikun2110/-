# -*- coding: utf-8 -*-

# 예외처리
# SyntaxError : 문법오류


# 결과 = eval("파이썬 코드")

try:
    x = eval("10 ** 3")
    print('x=', x)
    
    y = eval("10 *** 3") # 예외발생
    print('x=', x)
    
except SyntaxError as e:
    print("[예외발생] 문법오류:", e) # invalid syntax (<string>, line 1)
except:
    print("[예외발생] 알 수 없는 오류 발생")    

print("[종료]")    