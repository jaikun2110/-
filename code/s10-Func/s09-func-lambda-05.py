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

def calc(what, func, a, b):
    print(f"calc({what}): ", func(a, b))
    

# 함수:
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

#%%

calc("일반(홀수)", add, 1,3)
calc("일반(짝수)", add, 2,4)
calc("일반(곱셈)", mul, 2,4)

#%%

# 람다식 함수
calc("람다(홀수)", lambda a, b : a + b, 1,3)
calc("람다(짝수)", lambda a, b : a + b, 2,4)
calc("람다(곱셈)", lambda a, b : a * b, 2,4)


