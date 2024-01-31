# 세트 차집합(difference)
# a에서 b를 뺀 나머지 요소
# a에서 b에 있는 데이터를 제외하고 남은 요소
# d = a - b
# 메소드 : set.difference(...)

a = set("1234567890")
b = set("02468")

d = a - b
print(a)
print(b)
print(d) # {'1', '7', '9', '5', '3'}

#%%

d2 = a.difference(b)
print(d2)

#%%

d3 = b.difference(a)
print(d3) # set()

d4 = b - a
print(d4) # set