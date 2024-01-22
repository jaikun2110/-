"""isintance(표현식, type) 
자료형이 일치하는지 검사하고 True, False로 결과 알려줌
"""

pi=3.1
ps=str(type(pi))
pf=str(type(pi))
pt=type(pi)
print("float?", isinstance(pi, pt))
print("float?", isinstance(pi, float))
print("int?", isinstance(pi, int))
print("str?", isinstance(pi, str))
print("bool?", isinstance(pi, bool))

#%%

print("10/3:" , isinstance(10/3, float))
print("10//3:" , isinstance(10//3, float))
print("10//3:" , isinstance(10//3, int))