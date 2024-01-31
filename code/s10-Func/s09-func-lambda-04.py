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

def calc(what, func, *vals):
    # vals은 하나의 튜플이므로 튜플 전체가 하나의 인자로 전달
    # print(f"calc({what}): ", func(vals))
    
    # *vals : 튜플을 개별적인 인자로 분해(가변인자화)
    print(f"calc({what}): ", func(*vals))
    

# 함수: 가변인자 처리
def add(*vals):
    print('add: ', type(vals), vals)
    result = 0
    for val in vals:
        result += val
    return result

#%%

addition = add
print("addition:", addition(1,2,3,4,5))
#%%

calc("홀수", add, 1,3,5,7,9)
calc("짝수", add, 2,4,6,8,10)
