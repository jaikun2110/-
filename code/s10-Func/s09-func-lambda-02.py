# -*- coding: utf-8 -*-

# 함수 : 람다(lambda)
# inline 함수, 익명함수
# 함수형 프로그래밍(functional programming)에 활용
#
# 정의와 선언이 동시에 이루짐
# 정의선언: 함수변수 = lambda 파라미터 : 표현식
# 함수호출: 함수변수(파라미터)
# 결과리턴: 표현식의 처리 결과를 리턴


#%%

# 일반함수 정의
def add(a, b):
    print(f"일반함수: add({a}, {b})")
    return a + b

add(88,99)

#%%

# 위에 정의된 일한함수 add()는 사라짐

# 람다식 함수
# 함수 몸체의 표현식에 return이 숨어있다.
# add: 함수를 담고있는 변수
add = lambda a, b: a + b
d = add(10, 20)
print("람다함수 : add(10, 20)의 결과는?", d)

