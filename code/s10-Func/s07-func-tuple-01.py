# -*- coding: utf-8 -*-

# 함수: 가변인자
# 인자가 가변일 때 유용

# 최초 : a, b, c
# 파라미터 d를 추가하게 되면 호출할 때 오류 발생하여
# 오류를 예방하기 위해서 default value를 지정
# d = 0
def total(a, b, c, d=0):
    return a + b + c

print(total(10,20,30))

#%%

# 가변인자를 처리하도록 정의된 함수
# 인자를 튜플(tuple)로 받음
# 가변인자형: 파라미터 변수앞에 아스터리스크(*)를 붙임
def totals(*vals):
    print(f"totals() : type={type(vals)}, {vals}")
    
#%%

totals(10)   

#%%
totals(10,20,30)   
totals(10,20,30,40)   

#%%

a = (10,)
totals(a)
 