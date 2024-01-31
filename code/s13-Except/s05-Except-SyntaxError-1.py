# -*- coding: utf-8 -*-

# 예외처리
# SyntaxError : 문법오류

# 예외를 처리하지 못함
# 실행시간(runtime)에 예외를 잡지 못함

try:
    x = 10 *** 3  # SyntaxError: invalid syntax
    print('x=', x)
except SyntaxError as e:
    print("[예외발생] 문법오류:", e)    
except:
    print("[예외발생] 알 수 없는 오류 발생")    

print("[종료]")    