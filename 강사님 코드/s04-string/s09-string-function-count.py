# 문자열 함수
# 결과 = 문자열.함수()

# 문자 갯수 세기 : count()
s = "hobby"
print('count=', s.count('b'))
print("'hello'.count('l') :", "hello".count('l'))

#%%
b = "welcome to korea"
spcnt = b.count(' ')
print(f"'{b}'.count(' ') : {spcnt}")

#%%
tel = "010-1234-5678"
telcnt = tel.count('-')
print(f"'{tel}'.count('-') : {telcnt}")

#%% 

# 문자열 갯수
str = "abc,abc,hello,welcome to korea"
abccnt = str.count('abc')
ABCcnt = str.count('ABC') # 대소문자 구분
endcnt = str.count('end')

print(f"'{str}'.count('abc') : {abccnt}") # 2
print(f"'{str}'.count('ABC') : {ABCcnt}") # 0
print(f"'{str}'.count('end') : {endcnt}") # 0




