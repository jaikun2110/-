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

# 1회성 처리함수
# lambda를 괄호로 감싼 후 호출형태로 기술
# (lambda 파라미터 : 표현식)(인자)
print("람다함수: 10 * 20 ->", (lambda a, b: a * b)(10,20))
print("람다함수: 10 ** 3 ->", (lambda a, b: a ** b)(10,3))
