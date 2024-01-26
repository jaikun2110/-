# 딕셔너리
# 키(key)는 변하는 않는 값을 사용해야 한다.
#   - 리스트(list)는 사용할 수 없다.(값을 변경 가능)
#   - 중복을 허용하지 않는다.(유일한 값)

#%%

d1 = {}
d1[1] = '일'
d1['나이'] = 34

print(d1)

#%%

# TypeError: unhashable type: 'list'
lstk = [1,3,5]
print(lstk)
# d2 = {}
# d2[lstk] = '홀수'
# print(d2)

lstk[0] = -1
print(lstk)

#%%

sk = '문자열키'
print('sk:', id(sk), sk)

sv = '암호'
dx = {sk:sv}
print(dx)

# TypeError: 'str' object does not support item assignment
# sk[3] = '카'

sk = '문자키'
print('sk:', id(sk), sk)
print(dx)

#%%

dt = {}
dt['한글'] = '세종대왕'
dt['문자'] = 'ABCDEFG'
dt['숫자'] = 99
dt['튜플'] = (1,3,5)
dt['리스트'] = [2,4,6]
dt['사전'] = {'high':'높이', 'good':'좋은'}
dt['세트'] = set("1234567890")

print(dt)

print(dt['사전'])         # {'high': '높이', 'good': '좋은'}
print(dt['사전']['good']) # 좋은
print(dt['사전'].get('good')) # 좋은

dx = dt['사전']
print(dx, type(dx))
print(dx['high'], dx['good'])
print(dx.get('high'), dx.get('good'))

#%%

# 딕셔너리 전체 지우지
dt.clear()
dt = {}
