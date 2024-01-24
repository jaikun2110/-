
"""
셋의 교집합
연산자:&
set.intersection()


"""

s1 = set("12344567")
s2 = set("1234890")

s3 = s1 & s2
#= s3=s1.intersection(s2)

print(s1)
print(s2)
print(s3)


#%%

sl=list(s3)
sl.sort()

print(sl)

sl2=set(sl)

print(sl2)
#리스트로 정렬을 해도 세트로 변환하면 순서 바뀜