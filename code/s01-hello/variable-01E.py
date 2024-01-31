# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:45:42 2024

@author: YONSAI
"""

"""
[문제] 국어, 영어, 수학 점수의 값을 담을 수 있는 
변수 3개를 만들고 총합을 담을 수 있는 변수를 만들어
3과목의 점수를 넣어서 출력하라.
"""

#%%

kor = 100
eng = 90
math = 70
tot = kor + eng + math

print("국어:", kor)
print("영어:", eng)
print("수학:", math)
print('-' * 10)
print("합계:", tot)

#%%

# 평균
# 나누셈 연산자: 슬래시(/)
avg = tot / 3
print("평균:", avg)
print("평균:", tot / 3)   # 실수 나눗셈
print("평균:", tot // 3)  # 정수 나눗셈





