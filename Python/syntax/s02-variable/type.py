
"""자료형(type)
정수형(int) : 0, 음수, 양수
실수형(float) : 부동소수점, 지수형
논리형(bool) : True, False 대문자 이용해야함
문자형(str) : 문자, 나타낼때 (',  ")따옴표 쌍따옴표 이용함
객체형(object) : 사용자 지정 자료형

type(변수) 를이용하여 자료형을 알수있음

"""

#%%

#정수형

print(type(0))
print(type(-1))
print(type(10))

#%%

#실수형, 지수형

print(type(0.12))

print(type(3**3))# 3의 3제곱
print(type(3e2)) #3에 10의 2제곱을 곱함 e 대소문자 모두사용가능

#%%

#문자형

s1 = "쌍따옴표를 이용함"
s2 = '따옴표를 이용함'
s3 = "123"
print(type(s1))
print(type(s2))
print(type(s3))