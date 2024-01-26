# 논리형(boolean) : bool
# 참   : True
# 거짓 : False

t = True
f = False

print('t=', t)
print('f=', f)

#%%
a = t
b = f

print('a=', a)
print('b=', b)

#%%

# 같은가? : ==
print("a == t ->", a == t) # True
print("b == f ->", b == f) # True

#%%

# 같지 않는가? : !=
print("a != t ->", a != t) # False
print("b != f ->", b != f) # False

#%%

# 자료형? : type(변수)
print('t의 자료형?', type(t)) # <class 'bool'>
print('f의 자료형?', type(f)) # <class 'bool'>

#%%

# 같다(==), 같지않다(!=) 비교 결과는 bool 자료형

a = 1 == 1
b = 1 != 1
print(type(a))
print(type(b))

#%%







