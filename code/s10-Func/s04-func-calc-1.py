# -*- coding: utf-8 -*-


# 전역, 지역 변수
# global, local variable

tot = 0
lst = []

def func(a, b):
    global tot # 전역변수를 수정하겠다고 선언
    # 함수에서 전역변수를 참조 가능
    print('총합:', tot, id(tot))
    c = a + b
    tot += c
    lst.append(c)
    print("lst", lst, id(lst))
    return c

print(func(10, 20))
print(func(99, 100))

# NameError: name 'c' is not defined
# 변수(c) 함수(func) 안에서 선언된 지역변수
# print('c=', c)