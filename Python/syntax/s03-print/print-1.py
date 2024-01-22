# print(...)
# 내장함수(Built-In Function)

#%%
# 콘솔창에 메시지를 출력하는 함수
print("시작")
print() # 라인피드(엔터키 효과)
print("종료")

#%%
x = 10
y = 20
z = 30

# 각 인자들 사이에 공백문자를 넣어서 출력
print(x, y, z) # 결과: 10 20 30
print(x, y, z, sep=' ') # 결과: 10 20 30

#%%
print(x, y, z, sep='') # 결과: 102030

#%%

# 옵션: sep=',' 공백대신 콤마로 인자들을 구분해서 출력
print(x, y, z, sep=',') # 결과: 10,20,30
print(x, y, z, sep=', ') # 결과: 10,20,30

#%%

print(x, y, z, sep='-') # 결과: 10-20-30
print(x, y, z, sep="-") # 결과: 10-20-30



