# 부분집합
# a.issubset(b)
# a는 b의 부분집합인가?
# 결과 : True, False

a = {'서울', '대전', '대구', '부산', '제주'}
b = {'서울', '대전', '대구', '부산', '전주', '목포'}
c = {'서울', '대전', '대구', '부산'}
d = {'서울', '대전', '대구', '부산'}

#%%

# a의 '제주'는 b에 없다.
sab = a.issubset(b)
print("a는 b의 서브세트인가?", sab) # False

#%%
scb = c.issubset(b)
print("c는 b의 서브세트인가?", scb) # True

#%%

sca = c.issubset(a)
print("c는 a의 서브세트인가?", sca) # True

#%%

# 서로 같아도 서브집합
scd = c.issubset(d)
print("c는 d의 서브세트인가?", scd) # True

sdc = d.issubset(c)
print("d는 c의 서브세트인가?", sdc) # True
