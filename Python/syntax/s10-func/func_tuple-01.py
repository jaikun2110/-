"""

함수 가변인자
인자가 가변일때 유용
"""
def to(x,y,z):
    return x+y+z
print(to(10, 20, 30))



#%%
"""
가변인자를 처리하도록 정의됨
인자를 튜플로 받음
가변인자형:파라미터 변수앞에 아스터리스크(*)를 붙임
"""
def tos(*vals):
    print(type(vals),vals)
    result = 0
    for val in vals:
        result += val
    return result
tos(10,20,30,40)