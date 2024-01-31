# -*- coding: utf-8 -*-

# 함수
# [문제1]
# 더하기, 빼기, 나누기, 곱하기, 나머지
# 위의 연산을 수행하는 계산기 함수를 각각 정의하라.
# 호출하여 실행된는 결과는 예시하라.
#
# [문제2]
# 문제1에 정의된 함수를 호출한 총합을 리턴하는 함수를 정의하라.
# 문제1에 정의된 함수를 호출한 평균을 리턴하는 함수를 정의하라.
# 총합과 평균을 실행하는 결과를 예시하라.
#
# [문제3]
# 문제1을 재계산하는 함수를 정의하고 처리결과를 예시하라.

# [문제4] 이력 관리
# calc()에 전달된 인자를 그대로 히스토리에 보관하여
# 재계산을 수행하는 함수를 정의하고 처리결과를 예시하라.

#%%

totals = [] # 계산결과 누적
total = 0
count = 0

def comp(a, op, b):
    c = 0
    if op == '+':
        c = plus(a, b)
    elif op == '-':
        c = sub(a, b)
    elif op == '*':
        c = mul(a, b)
    elif op == '/':
        c = div(a, b)
    elif op == '%':
        c = sur(a, b)
        
    return c        

def calc(a, op, b):
    # 객체의 id가 변경되지 않기 때문에 global로 선언하지 않아도 된다.
    # global totals

    # UnboundLocalError: cannot access local variable
    # 'total' where it is not associated with a value
    # 전역변수를 수정하겠다.

    global total
    global count
            
    c = comp(a, op, b)
    count += 1       # 평균을 계산하기 위한 횟수 누적        
    total += c       # 계산결과 누적  
    totals.append((a, op, b)) # 계산결과 보관(재계산 용)
    return c

def tot(): # 총합
    return total

def avg(): # 평균
    return total / count
    
def recalc(): # 재계산
    t = 0
    for a, op, b in totals:
        c = comp(a, op, b)
        t += c

    return t, t / len(totals)

def plus(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a // b

def sur(a, b):
    return a % b

#%%

print(f"10 + 20 = {calc(10, '+', 20)}, tot({tot()})")
print(f"90 - 50 = {calc(90, '-', 50)}, tot({tot()})")
print(f"3 * 4 = {calc(3, '*', 4)}, tot({tot()})")
print(f"10 / 3 = {calc(10, '/', 3)}, tot({tot()})")
print(f"10 % 3 = {calc(10, '%', 3)}, tot({tot()})")

print("총합:", tot(), ", 평균:", avg(), ", 재계산:", recalc());
print("계산이력:", totals)
