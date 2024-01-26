# -*- coding: utf-8 -*-

# 반복문 : while

# [문제] while문을 이용하라.
# 1부터 100까지 1씩 연속으로 숫자를 증가시켜
# 3의 배수와 5의 배수를 각각 구하라.

n = 1
m = 100
m3 = []
m5 = []

while n <= m:
    if n % 3 == 0: # 3의 배수
        m3.append(n)
    if n % 5 == 0: # 5의 배수
        m5.append(n)
        
    n += 1

print("3의 배수:", m3)        
print("5의 배수:", m5)        
