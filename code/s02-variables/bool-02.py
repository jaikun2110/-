# bool
# ==, !=

# 비교의 결과는 bool
a = (3 == 3)
print(a, type(a)) # True <class 'bool'>

# 같지 않아야 참이여야 하는데
# 같기 때문에 거짓
b = (3 != 3)
print(b, type(b)) # False <class 'bool'>


#%%

s = ('홍길동' == "홍길동")
print(s, type(s)) # True <class 'bool'>