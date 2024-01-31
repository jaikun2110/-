# -*- coding: utf-8 -*-

# for문 한 줄로 작성하기

students = [1,2,3,4,5]

# [리스트 내포]
# 리스트 students에 들어 있는 각 요소에 
# 100을 더하여 리스트 만들기
students2 = [ i + 100 for i in students ]
print(students2)

#%%

# {세트 내포}
students3 = { i + 100 for i in students }
print(students3)

#%%

# 튜플로 처리하지 않음 : generator
students4 = ( i + 100 for i in students )
print(type(students4))
for obj in students4:
    print(obj, end=',') # 101,102,103,104,105,

#%%
# 튜플 내포
students5 = tuple( i + 100 for i in students )
print(students5)

#%%
# [문제]
# 리스트 내포를 쓰지 않고
# 각 요소에 100을 더하여 새로운 리스트를 만들어라.

result = [] # 빈리스트 생성
for n in students:
    result.append(n + 100)
    
print(result)    
