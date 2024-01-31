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
    return a + b

c = add(10, 20)
print("일반함수 : add(10, 20)의 결과는?", c)

#%%

# 람다식 함수
# lambda_add: 함수를 담고있는 변수
lambda_add = lambda a, b: a + b
d = lambda_add(10, 20)
print("람다함수 : lambda_add(10, 20)의 결과는?", d)

