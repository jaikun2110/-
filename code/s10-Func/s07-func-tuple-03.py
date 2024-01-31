# -*- coding: utf-8 -*-

# 함수: 가변인자
# 인자가 가변일 때 유용

#%%

# 가변인자를 처리하도록 정의된 함수
# 인자를 튜플(tuple)로 받음
# 가변인자형: 파라미터 변수앞에 아스터리스크(*)를 붙임
def totals(title, *vals):
    print(f"totals({title}) : type={type(vals)}, {vals}")
    result = 0
    for val in vals:
        result += val
    return title, result  # 총합을 리턴
    
#%%

print(totals("[홀수]", 1,3,5,7,9))
print(totals("[짝수]", 2,4,6,8,10))
 