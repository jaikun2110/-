# 변수(variable)
# 메모리의 저장공간
# 
# 변수이름 명명 규칙
# 문자(영문자, 한글)로 시작 또는 언더스코어(_)로 시작
# 문자와 숫자의 조합 가능
# 대소문자 구분
# 예약어는 사용할 수 없다.

# 변수에 값을 할당(assign)
# 할당연산자 : =
x=10 # x <- 10
y=20 # y <- 20

print(x) # 10
print(y) # 20

z = x + y # z <- x + y
print("z=", z) # z= 30

# 기존의 변수에 새로운 값을 넣으면
# 기존의 값을 사라지고 새로운 값으로 채워진다.
z = 50
print("z=", z) # z= 50

#%%

# 변수명으로 한글을 쓸 수 있지만 추천하지 않음
홍길동="조선의 의적"
print(홍길동)

#%%

# 특별한 경우 사용
# 멤버변수나 시스템 변수

# 달러기호($) 변수명으로 쓸 수 없다.
# SyntaxError: invalid syntax
# $xyz = 100

_xyz = 100
print(_xyz)

#%%
xyz = 200

print(_xyz)
print(xyz)

#%%

# 대소문자 구분
Xyz = 300
print(_xyz)
print(xyz)
print(Xyz)

