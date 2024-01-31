# -*- coding: utf-8 -*-

# 예외처리(Exception): try~except
"""
1. 잘못된 동작을 했을 때 오류가 발생에 대한 대응
2. 런타임 오류 처리(Runtime Error)
    - 실행할 때 발생하는 오류
    - 문법오류(Syntax Error)는 예외처리를 할 수 없다.
    - 파이썬은 인터프리터 방식이라 실행 할 때 문법 오류가 발생할 수 있다.
    - 구문오류는 예외처리에 해당하지 않는다.
3. 오류가 발생하면 프로그램이 중단되고 오류 메시지가 출력된다.
4. 예외처리를 하면 오류를 잡아서 중단없이 실행 가능하다.    
"""

#%%

name = '홍길동'

try:
    print("이름:", name)
    print("나이:", age) # NameError: name 'age' is not defined
except NameError as e:
    print("[예외발생] 선언되지 않은 변수를 사용했습니다.")
    print(e)


