# -*- coding: utf-8 -*-

# 함수

# 더하기 함수 정의
# 2개의 값을 받아서 더한 후 리턴
# 파라미터: a, b
# 리턴 : c
def plus(a, b):
    c = a + b
    return c


#%%
# 함수호출 : 반복호출에 편리
x = 99
y = 1
z = plus(x, y)
print(f"{z} = plus({x}, {y})")

#%%
print(plus(10,20))
print(plus(1,2))
print(plus(3,4))
print(plus(100,20))
print(plus(44,11))

#%%

# [주의]
# 파라미터의 갯수와 인자의 갯수가 일치
# 자료형이 일치

# TypeError: plus() missing 2 required positional arguments: 'a' and 'b'
# print(plus())

# TypeError: plus() missing 1 required positional argument: 'b'
# print(plus(10))

# TypeError: plus() takes 2 positional arguments but 3 were given
# print(plus(10,20,30))

#%%
# 문자열 더하기
print(plus("10","20")) # "1020"

#%%

# 서로 다른 자료형
# TypeError: can only concatenate str (not "int") to str
# c = "10" + 20
# print(plus("10",20))
