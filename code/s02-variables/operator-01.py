# 연산자
# 사칙연산 : +, -, /, *
# 정수나누기 : //
# 나머지 : %, divmod(x,y)
# 지수 : **

#%%

a = 10
b = 3
c = 20

print('a=', a)
print('b=', b)
print('c=', c)

#%%
x = a + b * c / 2
print(f"{a} + {b} * {c} / {2} : ", x)
print("a + b * c / 2 :", x)

y = a + ((b * c) / 2)
print(f"{a} + (({b} * {c}) / 2) :", y)
print("a + ((b * c) / 2) :", y)

z = b * c / 2 + a
print("b * c / 2 + a : ", z)

#%%

# 2진수 실수 연산은 오차가 발생할 수 있다.
# IEEE 754 규약 참조
r = a / b   # 실수 나눗셈 : 3.3333333333333335
n = a // b  # 정수 나눗셈
print(r, n)

#%%

# 제곱 : **
rs = a ** b
print(f"{a}의 {b} 제곱은?", rs)

rx = a * 0.1e3
print(f"{a}의 {b} 제곱은?", rx)


