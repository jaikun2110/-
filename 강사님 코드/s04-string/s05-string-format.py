# 문자열 포맷팅(String Formatting)
# 문자열 포맷 코드
# %s : 문자열(string)
# %c : 문자(character)
# %d : 정수(10진수, decimal)
# %f : 실수(float)
# %o : 8진수(octal)
# %x : 16진수(hexa-decimal)
# 
# 형식
# 포맷문자열 % 변수
# 포맷문자열 % (변수, ...)

#%%
num = 99

print("이 숫자는 정수 %d 입니다." % num)
print(f"이 숫자는 정수 {num} 입니다.")
print("이 숫자는 정수 {0} 입니다.".format(num))

#%%
name = '홍길동'
age = 34
userfmt = "이름이 (%s)인 사람의 나이는 (%d)세 입니다." % (name, age)
print(userfmt)

#%%

# '%'를 출력하기 그대로 출력하기 위해서는 
# '%%'와 같이 연속해서 기술한다.
sv = 50
print("오늘 눈이 올 확률은 (%d)%% 입니다." % sv)


