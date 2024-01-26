# -*- coding: utf-8 -*-

# [문제]
# for, range를 사용하여 다음의 합을 구하라.
# 1부터 10까지 연속된 숫자를 생성하여
# 홀수의 합과 짝수의 합을 각각 구하라.

#
s = 1  # 시작값
e = 11 # 종료값

odd = 0  # 홀수의 합
even = 0 # 짝수의 합

for n in range(s, e):
    if (n % 2) == 1: # 홀수
        odd += n
    else:
        even += n

print("홀수의 합:", odd)  # 25=1,3,5,7,9        
print("짝수의 합:", even) # 30=2,4,6,8,10

