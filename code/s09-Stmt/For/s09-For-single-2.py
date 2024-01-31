# -*- coding: utf-8 -*-

# for문 한 줄로 작성하기

lst = [1,2,3,4,5,6,7,8,9,10]

result = []
for n in lst:
    if n % 2 == 0: # 짝수
        result.append(n * n)
        
print(result)        

#%%

# [문제] 리스트 내포를 사용하라.
# 위 리스트에서 홀수 요소만 꺼내서 제곱한 후 새로운 리스트를 생성하라.
# for, if를 내포해서 사용
odd = [n*n for n in lst if n % 2 == 1] # 홀수만 처리
print(odd)




