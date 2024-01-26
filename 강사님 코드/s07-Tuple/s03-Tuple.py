# 튜플(tuple) 응용

a = 10
b = 99

# 위 변수 a, b의 값을 서로 교체 하려면?
t = a # 임시변수에 a 변수의 값을 대피

# 서로 교체
a = b
b = t

print('a=', a)
print('b=', b)

#%%

# 튜플을 이용하면 임시변수를 만들지 않고 
# 서로 변수의 값을 교체 가능
a, b = b, a
print("# 교체 후")
print('a=', a)
print('b=', b)

# 
