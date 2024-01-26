# 대칭 차집합(symmertic difference)
# 한 쪽에는 있지만 양쪽 모두에 있지 않은 요소
# 윗꺽쇠(circumflex)
# sd = a ^ b 
# 메소드 : a.symmeritc_difference(b)

a = {'서울', '대전', '대구', '부산', '제주'}
b = {'서울', '대전', '대구', '부산', '전주', '목포'}
c = {'서울', '대전', '대구', '부산', '제주'}

sd1 = a.symmetric_difference(b)
print(sd1)   # {'제주', '목포', '전주'}

sd2 = a ^ b
print(sd2) # {'제주', '전주', '목포'}

#%%

# [문제]
# 위의 세트 a, b를 이용하여
# 차집합, 합집합을 결합해서 대칭차집합을 구하라.

print(b - a) # {'전주', '목포'}
print(a - b) # {'제주'}

sd3 = (b - a) | (a - b)
print(sd3)



