# 튜플 슬라이싱

t = (1,3,5,7,9)

# 슬라이싱 결과도 튜플
t24 = t[2:4]

# 튜플을 수정 불가
# TypeError: 'tuple' object does not support item assignment
# t24[0] = 99

#%%

# 원본의 내용을 슬라이싱 된 데이터로 교체
t = t[2:4]
print(t)