# 자료형(type)
# 정수형(int): 0, 음수, 양수
# 실수형(float) : 부동소수점, 지수형
# 논리형(bool) : True, False
# 문자형(str) : 메시지 처리, 따옴표("", '')로 양쪽을 감싼 형태
# 객체형(class) : 사용자 자료형
#
# 자료형 검사 : type() 함수를 이용

#%%

# 정수형(int)
x = 0
print(type(x))
print(type(0))
print(type(-1))
print(type(+10))
print(type(10))


#%%

# float: 실수형, 지수형
pi = 3.141592
print(type(0.123))
print(type(pi))

# 지수형(e,E)
e = 0.123e3 # 0.123 * 10의 3승
E = 0.123E3 # 0.123 * 10의 3승
print(type(e), e) # 123.0
print(type(E), E) # 123.0

x = 10000000000.0
y = 1.0e10  # 1.0 * 10의 10승
z = 10.0 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10
print('x=', x, type(x)) # float
print('y=', y, type(y)) # float
print('z=', z, type(z)) # float

#%%

# 문자열(string) : str
s0 = '' # 빈문자열
s1 = "큰따옴표로 감싼 문자열"
s2 = '작은따옴표로 감싼 문자열'
s3 = '0.123'
s4 = "12345"

print(type(s0), s0)
print(type(s1), s1)
print(type(s2), s2)
print(type(s3), s3)
print(type(s4), s4)



