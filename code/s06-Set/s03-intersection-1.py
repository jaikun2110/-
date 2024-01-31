# 세트(set)의 교집합
# 연산자 : &
# 메소드 : set.intersection(...)

#%%

# 문자열을 세트형으로 변환
s1 = set("0123456789")
s2 = set("2468A")

# 양쪽에 모두 존재하는 값을 선택
s3 = s1 & s2

print(s1)
print(s2)
print(s3) # {'6', '8', '4', '2'}

#%%

s4 = s1.intersection(s2)
print(s4) # {'6', '8', '4', '2'}

#%%

# 정렬 : 리스트로 변환하여 정렬
sl = list(s4)
sl.sort()
print("정렬:", sl) # ['2', '4', '6', '8']

# 다시 세트로 변환하면 순서가 보장되지 않음
s5 = set(sl)
print(s5, type(s5))
