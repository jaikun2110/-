# -*- coding: utf-8 -*-

# 함수: 가변인자
# 인자가 가변일 때 유용

#%%

# 가변인자를 처리하도록 정의된 함수
# 인자를 튜플(tuple)로 받음
# 가변인자형: 파라미터 변수앞에 아스터리스크(*)를 붙임
def totals(*vals):
    print(f"totals() : type={type(vals)}, {vals}")
    result = 0
    for val in vals:
        result += val
    return result  # 총합을 리턴
    
#%%

print('totals:', totals(10,20,30))    # 60
print('totals:', totals(10,20,30,40)) # 100
 