# 튜플 더하기

# [문제]
# 아래의 튜플 데이터에서 인덱스 
# tx(2번째)의 데이터를 tv(10)으로 바꿔라.

tv = 10 # 바꿀 값
tx = 2  # 바꿀 위치
tp = (1,3,5,7,9)

print('tp:', tp)

#%%
# [방법1]
# TypeError: 'tuple' object does not support item assignment
# tp[tx] = tv

tl = list(tp)
tl[tx] = tv
tp = tuple(tl)
print(tp)

#%%

# [방법2] 슬라이싱을 이용하라.

tp1 = tp[:tx]    # (1,3)
tp2 = tp[tx+1:]  # (7,9)
tp = tp1 + (tv,) + tp2
print(tp)

#%%

tp = tp[:tx] + (tv,) + tp[tx+1:]
print(tp)
