"""
여집합(diffrence)

a에서 b를 뺀 나머지 요소

ex) c=a-b
"""

a=set("01234567")
b=set("2468")

c=a-b
#= c=a.diffrence(b)

print(c)

#%%

"""
대칭 차집합

한쪽에는 있지만 양쪽 모두에 있지 않은 요소

ex) c=a^b , a.symmertic_diffrence(b)

"""

a={'A','B','C','D','E',}
b={'C','D','E','F','G',}
c=a^b
print(c)


#%%
"""
a와 b셋을 이용하여 
차집합 합집합을 결합해서 대칭 차집합을 구하라


"""
c1=a-b
c2=b-a
c3=c1|c2

print(c3)


